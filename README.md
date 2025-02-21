# 🐍 Snake Classification App

## 📌 Overview
This Streamlit application classifies images of snakes as **Venomous** or **Non-Venomous** using a pre-trained deep learning model. Users can either **upload their own image** or **select from preset snake images** to get a prediction.

## 🚀 Features
- **Upload an Image**: Users can upload a snake image in JPG, PNG, or JPEG format.
- **Preset Images**: Users can select from a list of preloaded images.
- **Deep Learning Model**: Uses an EfficientNet-based Keras model (`.keras` format) for classification.
- **Real-time Predictions**: Displays the predicted class with confidence.

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Snake_Classification.git
cd Snake_Classification
```

### 2️⃣ Create & Activate a Virtual Environment
```bash
python -m venv myVenv
source myVenv/bin/activate   # On macOS/Linux
myVenv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
streamlit run main.py
```

## 📁 Project Structure
```
Snake_Classification/
│── models/
│   ├── Snake_Classification.keras  # Pre-trained model
│── preset_images/
│   ├── venomous1.jpg
│   ├── venomous2.jpg
│   ├── nonvenomous1.jpg
│   ├── nonvenomous2.jpg
│── main.py  # Streamlit application
│── requirements.txt
│── README.md
```

## 🧠 How It Works
1. **Image Selection**: User uploads an image or selects from preset options.
2. **Preprocessing**: The image is resized to `224x224` and normalized.
3. **Prediction**: The model classifies the image as **Venomous** or **Non-Venomous**.
4. **Results**: The predicted class is displayed with confidence.

## ✅ Example Output
```
Predicted Class: Venomous
```

## ⚡ Troubleshooting
- **File Not Found Error**: Ensure `Snake_Classification.keras` exists in the `models/` directory.
- **Module Not Found Error**: Run `pip install -r requirements.txt` to install missing dependencies.
- **Streamlit Not Found**: Install it using `pip install streamlit`.

## 🤝 Contributing
Pull requests are welcome! If you'd like to add features, feel free to fork the repo and create a PR.

## 📜 License
This project is licensed under the MIT License.

## 🔗 Contact
For questions or feedback, reach out at [your-email@example.com](dharmainak2003@gmail.com) or create an issue on GitHub.

---
Enjoy classifying snakes! 🐍🔥

