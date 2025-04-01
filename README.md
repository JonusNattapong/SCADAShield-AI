# SCADAShield-AI

โครงการพัฒนาระบบตรวจจับการบุกรุกด้วยปัญญาประดิษฐ์ (AI-based Intrusion Detection System - IDS) สำหรับเครือข่าย SCADA

## ภาพรวม

โครงการนี้มีเป้าหมายเพื่อสร้างโมเดล Machine Learning สำหรับตรวจจับความผิดปกติและการโจมตีทางไซเบอร์ในสภาพแวดล้อม SCADA/IoT โดยใช้ข้อมูลจำลอง (mock data) ที่สร้างขึ้นเพื่อเลียนแบบการจราจรเครือข่ายปกติและการโจมตีประเภทต่างๆ

## โมเดลที่ใช้

เริ่มต้นด้วยโมเดล Machine Learning มาตรฐาน เช่น:
*   Random Forest

(อาจมีการทดลองโมเดลอื่นๆ เพิ่มเติมในอนาคต)

## ชุดข้อมูล

ใช้ชุดข้อมูลจำลองที่สร้างขึ้นโดยสคริปต์ `notebooks/generate_mock_data.py` ซึ่งประกอบด้วยฟีเจอร์พื้นฐานของ network traffic และ label จำแนกประเภท (Normal, Scan, DoS, Injection) ไฟล์ข้อมูลจะถูกเก็บไว้ที่ `data/raw/mock_scada_data.csv`

## โครงสร้างโปรเจกต์

```
.
├── data/
│   ├── raw/          # เก็บข้อมูลดิบ (เช่น mock_scada_data.csv)
│   └── processed/    # เก็บข้อมูลที่ผ่านการประมวลผลแล้ว
├── models/           # เก็บโมเดลที่ฝึกสอนเสร็จแล้ว
├── notebooks/        # เก็บ Jupyter Notebooks หรือสคริปต์สำหรับการทดลองและพัฒนา
│   └── generate_mock_data.py # สคริปต์สร้างข้อมูลจำลอง
├── README.md         # ไฟล์นี้
└── ...               # ไฟล์อื่นๆ เช่น สคริปต์สำหรับ train/test model
```

## การติดตั้งและใช้งาน (เบื้องต้น)

1.  **Clone repository:**
    ```bash
    git clone <your-repo-url>
    cd SCADAShield-AI
    ```
2.  **ติดตั้ง Dependencies:** (ตรวจสอบให้แน่ใจว่ามี Python และ pip ติดตั้งอยู่)
    ```bash
    pip install pandas numpy scikit-learn # และไลบรารีอื่นๆ ที่จำเป็น
    ```
3.  **สร้างข้อมูลจำลอง:**
    ```bash
    python notebooks/generate_mock_data.py
    ```
4.  **(ขั้นตอนต่อไป)** พัฒนาและรันสคริปต์/notebook สำหรับการประมวลผลข้อมูล, ฝึกสอนโมเดล, และประเมินผล
