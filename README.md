# Term Project (team 14)
###### _written by ***Han Haebin, Kim Dayoon, Kim Sunyoung, Jung Soyeoun***_

---

## **Project Overview**
- **Goals**: Recognize face and blurs, apply a filter on it.
- **Step involved & Results**
    1. Find a person's face in the image.
    2. Print the results of the original image.
    3. Print the results of blurring the entire picture.
    4. Print a blur picture except for the human face.
    5. Print only human face.
    6. Print a filter on the picture.


## **Requirements (with versions I tested on)**
    1. python (3.10.4)
    2. opencv (4.6.0)
    3. matplotlib (3.6.2)


## **Demo images**
Result1 and Result2 print original image, blur the entire picture, blur picture except for the human face and print only human face.
The code can be viewed in the **'IMAGE_BLUR'** file.

**Result1**
![result1](https://user-images.githubusercontent.com/112797078/206885322-350bf293-1ee9-4f8f-ae9a-6702b9821555.png)

**Result2**
![result2](https://user-images.githubusercontent.com/112797078/206885375-d8a7c63d-7e79-4f23-90f9-d9bfa6049f26.png)



Result3 and Result4 print a filter on the picture.
The code can be viewed in the **'Filter'** file.

**Result3**

![result3](https://user-images.githubusercontent.com/112797078/206956572-6c1b39f2-5b3a-4856-803a-a84499a1b709.jpg)

**Result4**

![result4](https://user-images.githubusercontent.com/112797078/206956615-ef8d00c7-e904-4c02-b798-f4a510771c48.jpg)

## **Operation Process**
- Run with Python.

## **Changes and additions to the original project**
1. Change plt.imshow() to cv2.imshow()
2. Add code to filter pictures

---
## **Reference**
- image source:
    - first image: ps://www.pinterest.co.kr/pin/372109987965527920/feedback/?invite_code=32542b8d469f4e7db1d56c2fd94f92c7&sender_id=755197568673427164
    - second image: https://www.pinterest.co.kr/pin/542754192605297851/feedback/?invite_code=b8689c1d62804d37b493dea90809861b&sender_id=755197568673427164

- code reference: https://a292run.tistory.com/entry/Face-and-Background-Blurring-with-OpenCV-in-Python-1
