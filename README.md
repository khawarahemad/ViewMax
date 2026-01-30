# ViewMax - GitHub Profile Visitor Tool

A Python-based tool to visit GitHub profiles using Selenium WebDriver. Supports both macOS and Linux VPS environments.

## Features

- **Safe Mode**: Sequential visits with single browser instance
- **Extreme Mode**: Concurrent visits with multiple browser instances
- **Cross-Platform**: Works on macOS, Linux, and Windows
- **Progress Tracking**: Real-time progress bar and status updates
- **VPS Optimized**: Memory-optimized for server environments

## Installation

### Quick Setup (Linux VPS - Recommended)

```bash
# Clone the repository
git clone https://github.com/khawarahemad/ViewMax.git
cd ViewMax

# Run automated setup script
chmod +x setup_vps.sh
./setup_vps.sh
```

### Manual Setup

#### 1. Install System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip chromium-browser chromium-chromedriver
```

**macOS:**
```bash
brew install python3 chromedriver
```

#### 2. Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

## Usage

### For Linux/VPS (Recommended):
```bash
python3 ViewMax_Linux.py
```

### For macOS:
```bash
python3 ViewMax.py
```

### Running in Background (VPS):
```bash
nohup python3 ViewMax_Linux.py > output.log 2>&1 &

# Check progress:
tail -f output.log
```

## Modes

### Safe Mode (1)
- Sequential browser visits
- Lower resource usage
- Recommended for: Small VPS (1GB RAM)

### Extreme Mode (2)
- Concurrent browser visits
- Higher resource usage
- Recommended for: VPS with 2GB+ RAM
- Suggested concurrent browsers: 3-5 for 2GB, 10+ for 4GB+

## Requirements

- Python 3.6+
- Selenium 4.0.0+
- Chrome/Chromium Browser
- Chromedriver

## VPS Recommendations

| VPS RAM | Mode | Max Concurrent Browsers |
|---------|------|-------------------------|
| 1GB | Safe | N/A (Sequential) |
| 2GB | Extreme | 3-5 |
| 4GB+ | Extreme | 10-20 |

## Troubleshooting

### Chromedriver not found
```bash
which chromedriver
sudo ln -s /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver
```

### Memory issues on VPS
- Reduce concurrent browsers
- Use Safe Mode
- Check memory: `free -h`

## Files

- `ViewMax.py` - Original version (macOS-optimized)
- `ViewMax_Linux.py` - Cross-platform version (Linux/VPS-optimized)
- `setup_vps.sh` - Automated setup script for Linux VPS
- `requirements.txt` - Python dependencies

## License

MIT License

## Author

[@khawarahemad](https://github.com/khawarahemad)