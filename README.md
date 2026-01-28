# Cryptify 🔐

**Cryptify** is a modern, full-stack encryption and decryption web application that provides a user-friendly interface for securing data using industry-standard cryptographic algorithms. Built with Flask (Python) backend and a distinctive cyberpunk-themed frontend.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)

---

## 📋 Table of Contents

- [Features](#features)
- [Supported Algorithms](#supported-algorithms)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [Frontend Features](#frontend-features)
- [Security Considerations](#security-considerations)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### Core Functionality
- 🔒 **Encryption & Decryption**: Secure text and files using multiple algorithms
- 📝 **Dual Input Modes**: Support for both text strings and file uploads
- 🎛️ **Two Operation Modes**:
  - **Simple Mode**: Auto-generates encryption keys and IVs
  - **Advanced Mode**: Custom key and IV specification
- 💾 **Multiple Output Formats**: Binary and hexadecimal file outputs
- 📋 **Copy to Clipboard**: Quick copy for keys, IVs, and encrypted data
- 🔄 **Algorithm-Specific Validation**: Dynamic constraints based on selected algorithm
- 📥 **File Downloads**: Download encrypted/decrypted files instantly

### User Experience
- 🎨 **Distinctive Cyberpunk UI**: Neon-themed, animated interface
- 📱 **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- ⚡ **Real-time Feedback**: Loading animations and success notifications
- 🎯 **Smart Form Validation**: Prevents invalid configurations

---

## 🔐 Supported Algorithms

| Algorithm | Block Size | Key Sizes | Notes |
|-----------|------------|-----------|-------|
| **AES** (Advanced Encryption Standard) | 128 bits (16 bytes) | 128, 192, 256 bits | Industry standard, highly secure |
| **DES3** (Triple DES) | 64 bits (8 bytes) | 128, 192 bits | Legacy algorithm, still widely used |
| **Blowfish** | 64 bits (8 bytes) | 128, 192, 256 bits | Fast and flexible |
| **Twofish** | 128 bits (16 bytes) | 128, 192, 256 bits | AES finalist, very secure |

All algorithms use **CBC (Cipher Block Chaining)** mode for enhanced security.

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **PyCryptodome** - Cryptographic library for AES, DES3, Blowfish
- **LibTomCrypt** - C library for Twofish (via ctypes)
- **filetype** - File type detection

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with custom animations
- **JavaScript (Vanilla)** - Interactive functionality
- **Google Fonts** - Orbitron & Rajdhani typography

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- GCC compiler (for Twofish C library)

### Step 1: Clone the Repository

```bash
https://github.com/abhi-pillai/Cryptify_New.git
cd Cryptify_New
```

### Step 2: Install Python Dependencies

```bash
pip install flask flask-cors pycryptodome filetype
```

### Step 3: Compile Twofish Library

The Twofish algorithm requires a compiled C library:

```bash
# Install LibTomCrypt (if not already installed)
# On Ubuntu/Debian:
sudo apt-get install libtomcrypt-dev

# On macOS:
brew install libtomcrypt

# Compile the Twofish wrapper
gcc -shared -o libtwofish.so -fPIC twofish_to_py2.c -ltomcrypt
```

### Step 4: Create Necessary Directories

```bash
mkdir -p temp
mkdir -p templates
```

### Step 5: Move Frontend Files

```bash
# Move HTML files to templates directory
cp templates/*.html ./templates/
```

### Step 6: Run the Application

```bash
python app.py
```

The application will start on **http://localhost:5000**

---

## 📁 Project Structure

```
cryptify/
│
├── app.py                      # Main Flask application
├── Temporary.py                # Core encryption/decryption logic router
├── Simple.py                   # Simple mode encryption/decryption
├── Advance.py                  # Advanced mode encryption/decryption
├── utility.py                  # Helper functions (file conversion)
├── twofish.py                  # Twofish Python wrapper
├── twofish_to_py2.c           # Twofish C implementation
├── libtwofish.so              # Compiled Twofish library
│
├── templates/                  # Frontend HTML files
│   ├── index.html             # Landing page
│   ├── encryption.html        # Encryption interface
│   └── decryption.html        # Decryption interface
│
├── temp/                       # Temporary file storage (auto-created)
│
├── README.md                   # This file
└── requirements.txt            # Python dependencies
```

---

## 📖 Usage Guide

### Encrypting Data

#### **Simple Mode (Recommended for Beginners)**

1. Navigate to **http://localhost:5000/encrypt**
2. Choose input type:
   - **Text**: Enter your message directly
   - **File**: Upload a file
3. Select **Simple** mode
4. Choose your encryption algorithm (AES, DES3, Blowfish, or Twofish)
5. Select block size and key size (options auto-adjust based on algorithm)
6. Click **"Encrypt Data"**
7. **Important**: Save the generated key (and IV for some modes) - you'll need it for decryption!
8. Download encrypted files or copy hex values

#### **Advanced Mode (For Experienced Users)**

1. Follow steps 1-2 from Simple Mode
2. Select **Advanced** mode
3. Choose algorithm and parameters
4. **Provide your own encryption key and IV** (in hexadecimal format)
   - Key length must match selected key size
   - IV length must match selected block size
5. Click **"Encrypt Data"**
6. Download or copy your encrypted data

### Decrypting Data

#### **Simple Mode**

1. Navigate to **http://localhost:5000/decrypt**
2. Choose input type (Text or File)
3. Select **Simple** mode
4. Select the **same algorithm** used for encryption
5. Select the **same block size and key size** used for encryption
6. **Enter the decryption key** (from encryption step)
7. Click **"Decrypt Data"**
8. View or download the decrypted result

#### **Advanced Mode**

1. Follow steps 1-5 from Simple Mode decryption
2. Select **Advanced** mode
3. Enter both the **key** and **IV** used during encryption
4. Click **"Decrypt Data"**

### Important Notes

⚠️ **Critical Reminders**:
- Always save your encryption keys securely
- Use the exact same algorithm, block size, and key size for decryption
- In Advanced mode, both key and IV are required for decryption
- Keys and IVs must be in hexadecimal format

---

## 🔌 API Documentation

### Endpoints

#### `GET /`
- **Description**: Landing page
- **Returns**: HTML home page

#### `GET /encrypt`
- **Description**: Encryption interface
- **Returns**: HTML encryption page

#### `GET /decrypt`
- **Description**: Decryption interface
- **Returns**: HTML decryption page

#### `POST /uploader/`
- **Description**: Handle encryption requests
- **Content-Type**: `multipart/form-data`
- **Parameters**:
  - `ipmode`: `text` or `file`
  - `iptext`: Text to encrypt (if ipmode=text)
  - `ipfile`: File to encrypt (if ipmode=file)
  - `mode`: `simple` or `advanced`
  - `algorithm`: `1` (AES), `2` (DES3), `3` (Blowfish), `4` (Twofish)
  - `blocksize`: Block size in bytes
  - `keysize`: Key size in bytes
  - `kvalue`: Encryption key in hex (if mode=advanced)
  - `iv`: Initialization vector in hex (if mode=advanced)
- **Returns**: JSON
  ```json
  {
    "Data": {
      "encryptedMessage": "hex_string",
      "keyValue": "hex_string",
      "ivValue": "hex_string",
      "encryptedFile": "filename",
      "encryptedHexFile": "filename"
    }
  }
  ```
- **Error Codes**:
  - `401`: Incorrect key or IV length
  - `402`: Incorrect key length
  - `403`: Key was never assigned

#### `POST /downloader/`
- **Description**: Handle decryption requests
- **Content-Type**: `multipart/form-data`
- **Parameters**: Same as `/uploader/` but requires `kvalue` in both modes
- **Returns**: JSON
  ```json
  {
    "Data": {
      "decryptedMessage": "original_text",
      "decryptedFile": "filename"
    }
  }
  ```

#### `GET /download/<filename>`
- **Description**: Download encrypted/decrypted files
- **Parameters**: `filename` - Name of file in temp directory
- **Returns**: File download

---

## 🎨 Frontend Features

### Design Philosophy
- **Cyberpunk Aesthetic**: Neon colors, animated grids, glowing orbs
- **Distinctive Typography**: Orbitron (display) and Rajdhani (body)
- **Color-Coded Pages**:
  - Home: Cyan/Magenta gradient
  - Encryption: Green/Cyan theme
  - Decryption: Orange/Yellow theme

### Interactive Elements
- ✨ Smooth fade-in animations
- 🎯 Hover effects on cards and buttons
- 🔄 Loading spinners during operations
- 📋 One-click copy-to-clipboard
- 🎨 Dynamic form field updates
- 📱 Mobile-responsive layout

### Algorithm-Specific Validation
The frontend automatically adjusts available options based on the selected algorithm:
- Block size dropdown shows only valid sizes
- Key size dropdown shows only compatible sizes
- Prevents invalid combinations before submission

---

## 🔒 Security Considerations

### Best Practices

✅ **DO:**
- Use **AES-256** (256-bit key) for maximum security
- Store keys in a secure password manager
- Use unique keys for different data
- Delete temporary files after use
- Use HTTPS in production environments

❌ **DON'T:**
- Share encryption keys over insecure channels
- Reuse the same key for multiple files
- Store keys in plain text
- Use weak/predictable keys in Advanced mode
- Expose the `/temp` directory publicly

### Key Management
- **Simple Mode**: System generates cryptographically secure random keys
- **Advanced Mode**: User responsibility to provide strong keys
- Keys are displayed only once - save them immediately
- Lost keys = permanently encrypted data

### File Handling
- Files are temporarily stored in `/temp` directory
- Automatic cleanup on page load
- Ensure `/temp` has proper permissions (not world-readable)

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'Crypto'`
```bash
# Solution:
pip install pycryptodome
```

**Issue**: `libtwofish.so: cannot open shared object file`
```bash
# Solution: Recompile the Twofish library
gcc -shared -o libtwofish.so -fPIC twofish_to_py2.c -ltomcrypt
```

**Issue**: Decryption fails with padding error
- **Cause**: Incorrect key, IV, or algorithm settings
- **Solution**: Verify all encryption parameters match exactly

**Issue**: File upload doesn't work
```bash
# Solution: Check temp directory exists and has permissions
mkdir -p temp
chmod 755 temp
```

**Issue**: Copy to clipboard doesn't work
- **Cause**: Browser doesn't support Clipboard API or HTTP (not HTTPS)
- **Solution**: Use modern browser or enable HTTPS

**Issue**: CORS errors
- **Cause**: Flask-CORS not installed
- **Solution**: `pip install flask-cors`

---

## 🚀 Deployment

### Production Checklist

- [ ] Set `app.debug = False`
- [ ] Use a production WSGI server (Gunicorn, uWSGI)
- [ ] Enable HTTPS/SSL
- [ ] Set up proper file permissions
- [ ] Configure firewall rules
- [ ] Implement rate limiting
- [ ] Add logging and monitoring
- [ ] Regular security audits
- [ ] Backup encryption keys securely

---
## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **PyCryptodome** - Python cryptography library
- **LibTomCrypt** - Twofish implementation
- **Flask** - Web framework
- **Google Fonts** - Typography (Orbitron, Rajdhani)
- **Anthropic Claude** - AI assistance in development

---



## 📊 Version History

### v1.0.0 (Current)
- Initial release
- Support for AES, DES3, Blowfish, Twofish
- Simple and Advanced modes
- Text and file encryption
- Copy-to-clipboard functionality
- Algorithm-specific validation
- Responsive cyberpunk UI

---

<div align="center">

**Built with ❤️ for secure communications**

[⬆ Back to Top](#cryptify-)

</div>
