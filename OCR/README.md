# OCR

Optical Character Recognition (OCR) is used to convert images, pdf files to readable text format. Ocr analyzes the character properties like shape, pattern and translates them.

## OCR pipeline

![OCR pipeline](/OCR/images/pipeline.png)
[Image Source](https://theailearner.com/2019/05/28/optical-character-recognition-pipeline/)

### 1. Image preprocessing

Image preprocessing is an important steo. It clears noises and corrects rotation from the required image in order to perform further task.

### 2. Text detection

Text detection selects the regions having text in the image. There are different text detection methods which is divided into two categorizes:

1. Conventional (eg: MSER, SWT)
   It is based on manually generated features. Stroke width Transform (SWT) and Maximally Stable Extremal Regions (MSER) extracts text based on edge or extremal region.

2. Deep-learning based (eg: EAST, CTPN)
   Here, features are learnt from the training data. They are better than conventional because of better accuracy and adaptibility.

   Further, the deep learning based methods are classified into:

   1. Multi-step methods
   2. Simplified pipeline

   In simplified, Effective and Accurate Scene Text Detector (EAST) and Connectionist Text Proposal Network (CTPN).

For text detection, you will find Structured text(like book, resume) or unstructured text(different font, color and oriention). The text detection for unstructured text is called scene text detection.

There are 3 options for de tecting text:

1. Character-by-character detection
2. Word detection
3. Line detection

For resume, we will need line detection.

### 3. Text Recognition

To extract text from the regions selected in above process. There are many approaches for text recognition:

1. Deep-learning based
   1. CTC-based
   2. Attention based
2.

### 4. Restructuring

To create similar output as the input image to check the similarities. It is done by placing the text as per the properties of each text collected.

For resume, we need to extract words based on the given headings like name, address, skills, education etc.
From this extracted information, we can perform different applications like translation to different languages, search for a particular text or generate speech.

References:

[1](https://theailearner.com/2019/05/28/optical-character-recognition-pipeline/)
[2](https://www.docsumo.com/blog/text-recognition-algorithms)
