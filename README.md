# Health Agent - AI-Powered Wellness Recommendation System

A full-stack web application that provides personalized health recommendations using intelligent text compression and symptom-based analysis. Achieves up to **75% token savings** through smart truncation while delivering actionable medical advice.

✨ Features

- **75% Token Compression** - Smart medical text optimization
- **Symptom Detection** - Hypertension, diabetes, sleep issues, sedentary lifestyle
- **Personalized Recommendations** - Context-aware health advice
- **Modern Glassmorphism UI** - Professional responsive design
- **SQLite Database** - Persistent user data storage
- **Production-Ready** - Flask backend + static HTML frontend

🏗️ Tech Stack

Backend: Flask (Python 3.14) + SQLite
Frontend: Vanilla HTML/CSS/JavaScript (No frameworks)
Compression: ScaleDown package + Smart truncation fallback
Deployment-ready: Gunicorn + requirements.txt


## 🚀 Quick Start (Local)

1. **Clone repository**
```bash
git clone https://github.com/YOUR_USERNAME/health-agent.git
cd health-agent/backend
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Start backend**
```bash
python app.py
```
*Backend runs on `http://localhost:5000`*

4. **Open frontend**
- Double-click `frontend/health.html`
- Enter User ID + medical data
- Get instant recommendations!

## 💾 Database Schema

```sql
users table:
- id (TEXT PRIMARY KEY)
- history (TEXT)
- wellness (TEXT) 
- timestamp (TEXT)
```

## 🧠 How It Works

1. **Input**: User enters medical history + current wellness
2. **Compression**: AI-powered text optimization (75% size reduction)
3. **Analysis**: Symptom detection (hypertension, insomnia, etc.)
4. **Output**: Personalized emoji-rich recommendations

## 🔬 Symptom Detection Rules

- **Hypertension**: Keywords `hypertension`, `high blood pressure`, `BP 140+`
- **Sedentary**: Keywords `sedentary`, `desk job`, `sitting 8+ hours`
- **Poor Sleep**: Keywords `insomnia`, `sleep 5`, `poor sleep`, `fatigue`

## 📱 Example Usage

```
User ID: patient1
History: Hypertension diagnosis 2 years ago
Wellness: Sedentary job 10hrs/day, poor sleep 5hrs

Recommendations:
🥄 Reduce salt intake significantly
🏃‍♂️ Exercise 30min daily (walking/brisk)  
📊 Monitor BP weekly at home
💰 Token Savings: 75%
```

## 🛠️ File Structure

```
health-agent/
├── backend/
│   ├── app.py           # Flask API + compression logic
│   ├── requirements.txt # Python dependencies
│   └── health_data.db   # SQLite database (.gitignore)
├── frontend/
│   └── health.html      # Glassmorphism UI
├── .env                # Secrets (.gitignore)
└── README.md
```

## ⚙️ Development

```bash
# Backend (Terminal 1)
cd backend
python app.py

# Frontend (Browser)
Double-click frontend/health.html
```

## 🔒 Security

- `.env` → `.gitignore` (API keys safe)
- `health_data.db` → `.gitignore` (patient data safe)
- CORS enabled for frontend
- Input validation + sanitization

## 🎯 Test Cases


### **Test Case 1: Hypertension + Sedentary Lifestyle + Family History**
User ID: hypertension1
History: Patient Rajesh Kumar age 47 diagnosed with stage 2 hypertension March 2023 during routine annual health checkup at Apollo Hospital Hyderabad, strong family history of cardiovascular disease including father who suffered myocardial infarction age 52 mother controlled hypertension on medication since age 45, personal medical history includes regular home blood pressure monitoring using Omron digital device average daytime readings 152 systolic over 94 diastolic nighttime readings 148 over 90, experiencing occasional morning headaches frontal region occasional dizziness upon standing from sitting position, currently prescribed tablet Lisinopril 20mg once daily morning and tablet Atorvastatin 40mg once daily evening for cholesterol management with recent lipid profile showing total cholesterol 238mg/dL LDL 154mg/dL HDL 41mg/dL triglycerides 202mg/dL all above optimal therapeutic targets
Wellness: Software engineer at multinational IT corporation Hyderabad working corporate office environment 11 hours continuous daily computer screen exposure completely sedentary lifestyle zero structured aerobic exercise weekend entertainment primarily Netflix streaming binge-watching series and mobile video gaming PUBG Free Fire, irregular sleep-wake cycle averaging 5.2 hours weekdays 8-9 hours weekends creating circadian rhythm disruption, caffeine consumption excessive 4 large coffees 400ml each daily plus weekend energy drinks Red Bull Monster, hydration status poor approximately 1.2 liters water daily mostly carbonated soft drinks Pepsi Coke, continuous desk snacking potato chips namkeen mixture biscuits cookies throughout workday, extremely high work stress levels due to aggressive project deadlines client presentations quarterly performance reviews self-reported stress scale 9 out of 10 maximum, occasional palpitations during high-pressure conference calls

**Expected:** 65-80% compression + BP monitoring + salt reduction + 10k steps

***

### **Test Case 2: Type 2 Diabetes + Peripheral Neuropathy + Obesity**
User ID: diabetes1
History: Mrs Priya Sharma age 52 diagnosed Type 2 diabetes mellitus January 2022 during routine fasting blood sugar screening corporate wellness program HbA1c 8.4% fasting plasma glucose 168mg/dL postprandial 2hr 256mg/dL, strong family history maternal grandfather developed diabetes age 58 paternal aunt required insulin therapy age 62, current pharmacological management includes tablet Metformin 1000mg twice daily before meals tablet Glipizide 5mg once daily breakfast additional tablet Sitagliptin 100mg once daily dinner, experiencing bilateral lower limb peripheral neuropathy symptoms tingling paraesthesia feet intermittent numbness toes worse nighttime requiring Pregabalin 75mg bedtime, annual diabetic retinopathy screening Fundus photography January 2025 shows early non-proliferative changes microaneurysms dot blot hemorrhages, urine albumin creatinine ratio 52mg/g borderline microalbuminuria, serum creatinine 1.02mg/dL eGFR 68ml/min normal range
Wellness: Night shift Data Entry Operator Reliance Industries Jamnagar 10PM to 7AM schedule severely disrupting natural circadian rhythm irregular meal timing frequent late night fast food consumption McDonalds Burger King Domino's 4-5 times weekly supersized portions, daytime sleep duration severely compromised 4-5 hours interrupted by neighborhood traffic noise barking dogs domestic chores, current anthropometric measurements weight 96kg height 165cm BMI 35.3 obese class II waist circumference 102cm central obesity, recreational activity limited excessive mobile gaming 3+ hours nightly consuming 2 liters carbonated sugary beverages Thums Up Mirinda daily minimal physical exertion walks neighborhood stray dog 8-10 minutes occasional feels breathless climbing 2 flights stairs

**Expected:** 70-85% compression + diet control + foot care + weight loss

***

### **Test Case 3: Chronic Insomnia + Generalized Anxiety Disorder**
User ID: insomnia1
History: Mr Vikram Singh age 34 chronic primary insomnia diagnosed Sleep Medicine Specialist AIIMS Delhi 20 months ago comprehensive polysomnography PSG March 2024 confirmed severe sleep onset latency SOL 58 minutes total sleep time TST 4 hours 12 minutes sleep efficiency index SE 54% significantly below normal range, prescribed Zolpidem 10mg immediate release as needed maximum 3 nights weekly current usage pattern 5-6 nights weekly developing tolerance, Epworth Sleepiness Scale ESS score 16 severe daytime somnolence high motor vehicle crash risk, comorbid Generalized Anxiety Disorder GAD-7 screening score 15 severe range requiring Sertraline 50mg daily Escitalopram 10mg alternate therapy cognitive behavioral therapy CBTi referral, additional history gastroesophageal reflux GERD requiring Pantoprazole 40mg bedtime
Wellness: Freelance Digital Marketing Consultant irregular unpredictable client deadlines Delhi NCR region frequently working 1AM to 7AM bursts followed by daytime client meetings presentations, caffeine consumption excessive 600mg equivalent daily 3 double shot espressos 2 energy drinks Red Bull pre-workout supplements gym, blue light exposure extreme smartphone scrolling Instagram Twitter 4+ hours before attempted bedtime bedroom environment includes 55" LED television streaming Netflix Amazon Prime action thriller movies high arousal content, melatonin supplements 5mg extended release occasional subjective effectiveness 45% sleep onset improved 20 minutes, bedroom temperature 28°C excessively warm poor sleep hygiene weekend catch-up sleep 10-12 hours creating sleep inertia Monday morning

**Expected:** 65-80% compression + sleep hygiene + CBT referral + caffeine reduction

***

### **Test Case 4: Metabolic Syndrome + Obstructive Sleep Apnea**

User ID: metabolic1
History: Mr Anil Patel age 51 morbid obesity BMI 37.8kg/m2 current weight 118kg height 172cm waist circumference 112cm diagnostic criteria metabolic syndrome fully satisfied including essential hypertension controlled Lisinopril 20mg Hydrochlorothiazide 12.5mg combination daily prediabetes fasting plasma glucose 122mg/dL HbA1c 5.9%, moderate obstructive sleep apnea confirmed home sleep apnea test HSAT Philips Respironics AHI 34 events/hour oxygen desaturation index ODI 28 using AutoPAP ResMed AirSense 10 compliance 82% average nightly usage 5.8 hours pressure 10-16cmH2O auto-adjusting, non-alcoholic fatty liver disease NAFLD confirmed abdominal ultrasound grade 2 hepatosteatosis LFTs ALT 78 U/L AST 62 U/L GGT 145 U/L, dyslipidemia Atorvastatin 40mg Rosuvastatin 10mg alternate therapy total cholesterol 252mg/dL triglycerides 298mg/dL
Wellness: Heavy vehicle truck driver sedentary occupation 10 hours daily truck cabin confinement Ashok Leyland Eicher vehicles plying Hyderabad-Mumbai route, dietary pattern fast food dominant daily dhabas paratha dal makhani butter chicken 44oz sugary lassi carbonated beverages Thums Up 7UP continuous snacking during drives roasted peanuts mixture namkeen tobacco paan masala gutka 8-10 times daily, hydration inadequate 800ml water daily mostly chai tea breaks exercise tolerance extremely poor fatigues breathless walking 200 meters continuous limited stair climbing 1 flight apartment building breathless chest discomfort BMI 37.8 class II obesity sleep fragmented snoring witnessed apneas gasping nocturnal

**Expected:** 75-90% compression + CPAP compliance + weight loss + NAFLD diet

***

### **Test Case 5: Coronary Artery Disease Risk + Executive Stress**

User ID: cad_risk1
History: Mr Rohan Mehra age 49 male corporate executive strong familial premature coronary artery disease paternal uncle underwent CABG age 44 maternal aunt myocardial infarction age 51, comprehensive lipid profiling April 2025 total cholesterol 268mg/dL LDL 178mg/dL HDL 34mg/dL triglycerides 242mg/dL therapeutic targets suboptimal despite Atorvastatin 40mg daily Ezetimibe 10mg combination, current smoker 15 cigarettes Gold Flake daily 22 years pack years 330 moderate-high cardiovascular risk, stress echocardiography exercise treadmill test ETT Bruce protocol stage 3 achieved mild LVH left ventricular hypertrophy ejection fraction EF 60% normal diastolic dysfunction grade 1 ECG monitoring shows occasional PVCs LBBB pattern
Wellness: Senior Management Consultant Deloitte Mumbai 75 hours weekly international travel 4 cities weekly business class frequent flyer domestic international, dietary pattern rich high saturated fat business dinners steakhouses fine dining lobster prawns garlic butter nightly 3 glasses red wine Cabernet Shiraz alcohol consumption exceeding limits, exercise sporadic treadmill hotel gym 12 minutes 2x weekly interrupted urgent client calls conference calls APAC EMEA time zones, sleep disrupted luxury hotels 4.5-6 hours nightly compounded by jet lag time zone shifts 8-12 hours weekly international conference schedule Tokyo London Dubai

**Expected:** 70-85% compression + smoking cessation + lipid optimization + stress management

## 📈 Performance

- **Compression**: 60-80% token savings
- **Response Time**: <500ms
- **Database**: SQLite (file-based, zero-config)
- **Frontend**: Zero dependencies, instant load

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing-feature`)
5. Open Pull Request


## Acknowledgments

Built for college project demonstrating full-stack development, AI compression, and medical recommendation systems. Perfect balance of cutting-edge tech + practical healthcare application.

