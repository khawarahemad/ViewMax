#!/bin/bash

echo "================================================"
echo "   ViewMax - Automated VPS Setup Script"
echo "================================================"
echo ""

# Detect OS
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$NAME
else
    echo "❌ Cannot detect OS. This script supports Ubuntu/Debian."
    exit 1
fi

echo "�� Detected OS: $OS"
echo ""

# Update system
echo "🔄 Updating system packages..."
sudo apt-get update -qq

# Install Python3 and pip
echo "🐍 Installing Python3 and pip..."
sudo apt-get install -y python3 python3-pip > /dev/null 2>&1

# Install Chrome/Chromium and Chromedriver
echo "🌐 Installing Chromium and Chromedriver..."
sudo apt-get install -y chromium-browser chromium-chromedriver > /dev/null 2>&1

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt > /dev/null 2>&1

# Verify installation
echo ""
echo "✅ Verifying installation..."

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✓ Python: $PYTHON_VERSION"
else
    echo "❌ Python3 not found"
    exit 1
fi

# Check Chromium
if command -v chromium-browser &> /dev/null; then
    CHROME_VERSION=$(chromium-browser --version)
    echo "✓ Chromium: $CHROME_VERSION"
elif command -v google-chrome &> /dev/null; then
    CHROME_VERSION=$(google-chrome --version)
    echo "✓ Chrome: $CHROME_VERSION"
else
    echo "❌ Chrome/Chromium not found"
    exit 1
fi

# Check Chromedriver
if command -v chromedriver &> /dev/null; then
    DRIVER_VERSION=$(chromedriver --version)
    echo "✓ Chromedriver: $DRIVER_VERSION"
else
    echo "❌ Chromedriver not found"
    exit 1
fi

# Check Selenium
if python3 -c "import selenium" 2> /dev/null; then
    SELENIUM_VERSION=$(python3 -c "import selenium; print(selenium.__version__)")
    echo "✓ Selenium: $SELENIUM_VERSION"
else
    echo "❌ Selenium not installed"
    exit 1
fi

echo ""
echo "================================================"
echo "   ✅ Setup Complete!"
echo "================================================"
echo ""
echo "You can now run ViewMax:"
echo "  python3 ViewMax_Linux.py"
echo ""
echo "Or run the original (macOS version):"
echo "  python3 ViewMax.py"
echo ""