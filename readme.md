<h1>สรุปบทความ (text-summarization)</h1>

![alt text](/images/variables.png)

## ขั้นตอนการทำ text-summarization
- เตรียมข้อมูล
- จัดการลบสิ่งไม่จำเป็นสำหรับข้อมูลที่เตรียมไว้ (เว้นวรรค, ตัวเลข บลาๆ)
- แบ่งบทความนั้นๆ เป็นทีละประโยค(แบ่งตามที่ลงท้ายด้วยจุด)
- ทำการแบ่งประโยคเป็นแต่ละคำแล้วทำการนับคำที่ซ้ำกัน
- ทำการหา weigth โดยเอาคาแต่ละค่า / ค่าสูงสุดที่นับได้
- ทำการรวมคะแนนของแต่ละประโยคโดยเอาคะแนนของแต่ละคำในประโนคมารวมกัน

## Lib
[urllib.request](https://docs.python.org/3/library/urllib.request.html)=> ดึงข้อมูล

[beautifulsoup4](https://pypi.org/project/beautifulsoup4/) => ทำ HTML parser

[https://www.nltk.org/](https://www.nltk.org/) => จัดการ text (การแบ่งคำ, แบ่งประโยค จากบทความที่ได้)



