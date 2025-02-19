# HackDork

## परिचय

HackDork हा एक स्वयंचलित Google Dorking साधन आहे जो Playwright वापरून वेब पृष्ठांवरून संभाव्य दुवे काढतो. हे सुरक्षा संशोधक आणि ethical hackers विविध Google dorks वापरून गुप्तचर कार्यक्षमता सुधारण्यास मदत करते.

## वैशिष्ट्ये

- स्वयंचलित Google Dorking
- एकाच वेळी एकाधिक ब्राउझर टॅबसह समांतर कार्यक्षमता
- वर्गीकृत डॉर्क प्रकार (उदा. एक्स्पोज केलेली फाईल्स, असुरक्षा, लॉगिन पृष्ठे इ.)
- कार्यक्षम निकाल काढणे आणि सत्यापन
- डीबगिंग आणि देखरेखीसाठी लॉगिंग

## प्रतिष्ठापन

### पूर्वापेक्षित गोष्टी

तुमच्या Kali Linux मशीनवर खालील गोष्टी असणे आवश्यक आहे:

- Python 3.7+
- Playwright
- Requests
- Random
- Logging

### GitHub रेपॉजिटरी


```bash
git clone https://github.com/Prathameshsci369/HackDork.git
```

### Playwright प्रतिष्ठापीत करा

```bash
pip install playwright requests random
playwright install
```



## वापर

### HackDork चालवा

```bash
python dorking.py
```

तुम्हाला डोमेन प्रविष्ट करण्यास आणि विशिष्ट डॉर्क प्रकार निवडण्यास सांगितले जाईल.

### उदाहरण रन

```bash
python dorking.py
Enter the domain to perform dorking on: example.com
Available dork types:
1: Information Gathering
2: Exposed Files
...
Enter the numbers corresponding to the dork types you want to use: 1
2
3
```



## परवाना (License)

MIT परवाना

```
MIT License

Copyright (c) 2025 HackDork Developers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## अस्वीकरण

हे साधन केवळ सुरक्षा संशोधन आणि ethical hacking  हेतूने तयार करण्यात आले आहे. परवानगीशिवाय प्रणालींवर याचा वापर करणे बेकायदेशीर आहे आणि ते कठोरपणे निषिद्ध आहे.

