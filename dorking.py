import requests
import logging
import random
import time
from playwright.sync_api import sync_playwright
from dorks import Dorks

class DorkingTool:
    def __init__(self):
        """Initialize the DorkingTool with logging and dork mappings"""
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        self.dork_mapping = {
            1: "get_info_dorks",
            2: "get_exposed_files_dorks",
            3: "get_vulnerability_dorks",
            4: "get_camera_iot_dorks",
            5: "get_cloud_storage_dorks",
            6: "get_code_docs_dorks",
            7: "get_subdomain_dorks",
            8: "get_open_directories_dorks",
            9: "get_sensitive_files_dorks",
            10: "get_sql_error_dorks",
            11: "get_private_routers_dorks",
            12: "get_login_pages_dorks",
            13: "get_error_pages_dorks",
            14: "get_backup_files_dorks",
            15: "get_all_dorks"
        }

    def google_dork(self, domain, dork_types):
        """Perform Google dorking using Playwright with parallel tab execution"""
        self.logger.info(f"Starting dorking for domain: {domain} with types: {dork_types}")
        
        dorks_instance = Dorks(domain)
        dorks = []
        for dork_type in dork_types:
            if dork_type not in self.dork_mapping:
                error_msg = f"Invalid dork type. Choose from: {', '.join(map(str, self.dork_mapping.keys()))}"
                self.logger.error(error_msg)
                raise ValueError(error_msg)
            dork_method = getattr(dorks_instance, self.dork_mapping[dork_type])
            dorks.extend(dork_method())
        
        self.logger.info(f"Generated {len(dorks)} dorks for search")
    
        results = []
        with sync_playwright() as p:
            self.logger.info("Initializing Playwright browser")
            try:
                # Initialize the browser with specific settings
                # ब्राउझर विशिष्ट सेटिंग्जसह प्रारंभ करा
                browser = p.chromium.launch(
                    headless=False,  # Make browser visible for debugging
                    # डीबगिंगसाठी ब्राउझर दृश्यमान करा
                    args=[
                        '--disable-blink-features=AutomationControlled',
                        '--no-sandbox',
                        '--disable-setuid-sandbox',
                        '--disable-dev-shm-usage',
                        '--disable-gpu',
                        '--disable-software-rasterizer',
                        '--disable-extensions',
                        '--window-size=1920,1080',
                        '--start-maximized'
                    ],
                    slow_mo=100  # Add delay between actions
                    # क्रियांच्या दरम्यान विलंब जोडा
                )
                context = browser.new_context(
                    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    viewport={'width': 1366, 'height': 768}
                )
                self.logger.info("Browser context created successfully")
        
            except Exception as e:
                self.logger.error(f"Failed to initialize browser: {str(e)}")
                raise

            # Process dorks in parallel using multiple tabs
            # अनेक टॅब्स वापरून डॉर्क्स समांतर प्रक्रियेत करा
            max_tabs = 5
            active_tabs = []
            
            for i, dork in enumerate(dorks):
                if len(active_tabs) >= max_tabs:
                    # Wait for the first tab to complete
                    # पहिला टॅब पूर्ण होण्याची प्रतीक्षा करा
                    page = active_tabs.pop(0)
                    try:
                        # Try multiple selectors with 8 second timeout
                        # 8 सेकंदाच्या टाइमआउटसह एकाधिक सिलेक्टर्स वापरून पहा
                        try:
                            page.wait_for_selector('div.g', timeout=8000)
                        except:
                            try:
                                page.wait_for_selector('div#search', timeout=8000)
                            except:
                                try:
                                    page.wait_for_selector('div#rso', timeout=4000)
                                except:
                                    self.logger.warning("No results found within timeout, closing tab")
                                    page.close()
                                    continue
                    except Exception as e:
                        self.logger.warning(f"Error waiting for results: {str(e)}")
                        page.close()
                        continue
                    
                    # Extract results from completed tab
                    # पूर्ण झालेल्या टॅबमधून निकाल काढा
                    try:
                        links = page.query_selector_all('div.g a')
                        self.logger.info(f"Found {len(links)} potential results")
                        for link in links[:10]:
                            try:
                                href = link.get_attribute('href')
                                if href and href.startswith('http'):
                                    try:
                                        response = requests.get(href, timeout=10)
                                        if response.status_code == 200:
                                            results.append(href)
                                            self.logger.debug(f"Valid URL found: {href}")
                                    except Exception as e:
                                        self.logger.warning(f"Error validating URL {href}: {str(e)}")
                                        continue
                            except Exception as e:
                                self.logger.warning(f"Error extracting link: {str(e)}")
                                continue
                    except Exception as e:
                        self.logger.error(f"Error finding search results: {str(e)}")
                    
                    page.close()
                
                # Create new tab for current dork
                # वर्तमान डॉर्कसाठी नवीन टॅब तयार करा
                try:
                    self.logger.info(f"Processing dork {i+1}/{len(dorks)}: {dork}")
                    new_page = context.new_page()
                    
                    # Add retry logic for Google search
                    # Google शोधासाठी पुनःप्रयत्न लॉजिक जोडा
                    max_retries = 3
                    for attempt in range(max_retries):
                        try:
                            new_page.goto("https://www.google.com", timeout=120000)
                            new_page.wait_for_selector('textarea[name="q"]', timeout=60000)
                            break
                        except Exception as e:
                            if attempt == max_retries - 1:
                                raise
                            self.logger.warning(f"Retry {attempt + 1} for Google search")
                            time.sleep(5)
                    
                    new_page.keyboard.type(dork, delay=10)
                    new_page.keyboard.press("Enter")
                    
                    # Wait for results with 8 second timeout
                    # 8 सेकंदाच्या टाइमआउटसह निकालांची प्रतीक्षा करा
                    try:
                        try:
                            new_page.wait_for_selector('div.g', timeout=8000)
                        except:
                            try:
                                new_page.wait_for_selector('div#search', timeout=8000)
                            except:
                                try:
                                    new_page.wait_for_selector('div#rso', timeout=8000)
                                except:
                                    self.logger.warning("No results found within timeout, closing tab")
                                    new_page.close()
                                    continue
                        active_tabs.append(new_page)
                    except Exception as e:
                        self.logger.warning(f"Timeout waiting for results: {str(e)}")
                        new_page.close()
                        continue

                except Exception as e:
                    self.logger.error(f"Error processing dork {dork}: {str(e)}")
                    if 'new_page' in locals():
                        new_page.close()

            # Process remaining tabs
            # उर्वरित टॅब्स प्रक्रिया करा
            while active_tabs:
                page = active_tabs.pop(0)
                try:
                    # Wait for results with 5 second timeout
                    # 5 सेकंदाच्या टाइमआउटसह निकालांची प्रतीक्षा करा
                    try:
                        page.wait_for_selector('div.g', timeout=5000)
                    except:
                        try:
                            page.wait_for_selector('div#search', timeout=8000)
                        except:
                            try:
                                page.wait_for_selector('div#rso', timeout=5000)
                            except:
                                self.logger.warning("No results found within timeout, closing tab")
                                page.close()
                                continue
                except Exception as e:
                    self.logger.warning(f"Timeout waiting for results: {str(e)}")
                    page.close()
                    continue
                
                try:
                    links = page.query_selector_all('div.g a')
                    self.logger.info(f"Found {len(links)} potential results")
                    for link in links[:10]:
                        try:
                            href = link.get_attribute('href')
                            if href and href.startswith('http'):
                                try:
                                    response = requests.get(href, timeout=10)
                                    if response.status_code == 200:
                                        results.append(href)
                                        self.logger.debug(f"Valid URL found: {href}")
                                except Exception as e:
                                    self.logger.warning(f"Error validating URL {href}: {str(e)}")
                                    continue
                        except Exception as e:
                            self.logger.warning(f"Error extracting link: {str(e)}")
                            continue
                except Exception as e:
                    self.logger.error(f"Error finding search results: {str(e)}")
                
                page.close()

            try:
                context.close()
                browser.close()
                self.logger.info("Browser context closed successfully")
            except Exception as e:
                self.logger.error(f"Error closing browser: {str(e)}")
        
        return list(set(results))

# Main function
if __name__ == "__main__":
    dork_tool = DorkingTool()
    target_domain = input("Enter the domain to perform dorking on: ")
    print("Available dork types:")
    for key, value in dork_tool.dork_mapping.items():
        print(f"{key}: {value.replace('get_', '').replace('_dorks', '').replace('_', ' ').title()}")
    
    dork_types = []
    print("Enter the numbers corresponding to the dork types you want to use (press Enter after each number, and press Enter twice to start):")
    while True:
        dork_type = input()
        if dork_type == "":
            if len(dork_types) > 0:
                break
            else:
                print("Please enter at least one dork type.")
        else:
            try:
                dork_type = int(dork_type)
                if dork_type in dork_tool.dork_mapping:
                    dork_types.append(dork_type)
                else:
                    print(f"Invalid dork type. Choose from: {', '.join(map(str, dork_tool.dork_mapping.keys()))}")
            except ValueError:
                print("Please enter a valid number.")

    try:
        results = dork_tool.google_dork(target_domain, dork_types)
        print("\nClean Dorking Results:")
        for result in results:
            print(f"- {result}")
    except ValueError as e:
        print(f"Error: {e}")