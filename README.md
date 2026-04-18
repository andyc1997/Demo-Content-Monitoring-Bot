# RTHK News Scraper & AI Analyzer

A sophisticated web scraping and AI-powered news analysis system built with Robot Framework and integrated with Deepseek's large language model for automated content processing and insights generation.

## Overview

This project demonstrates advanced automation engineering by combining:
- **Web Scraping**: Automated extraction of news content from RTHK (Radio Television Hong Kong) using Selenium WebDriver
- **Data Processing**: Structured JSON output with timestamped data collection
- **AI Integration**: Deepseek LLM-powered content analysis for thematic insights and trend identification
- **Test Automation**: Robot Framework-based test suites with comprehensive logging and reporting

## Key Features

### Technical Architecture
- **Robot Framework**: Keyword-driven test automation with SeleniumLibrary integration
- **Selenium WebDriver**: Headless Chrome automation for reliable web scraping
- **Python Integration**: Custom libraries for JSON processing and API interactions
- **LLM Analysis**: Deepseek API integration for intelligent content summarization
- **Modular Design**: Separated concerns between scraping, data processing, and analysis

### Automation Capabilities
- Automated browser management with error handling and timeouts
- Dynamic content extraction from complex web structures
- Timestamped data collection with conflict-free file naming
- Comprehensive logging with HTML/XML reports
- Cross-platform compatibility (Windows/Linux/Mac)

### AI-Powered Insights
- Thematic analysis of news content
- Pattern recognition across multiple articles
- Structured reporting with key developments and trends
- English-language analysis output for global accessibility

## Technology Stack

- **Framework**: Robot Framework 6.1.1
- **Web Automation**: SeleniumLibrary 6.8.0, Selenium 4.43.0
- **AI Integration**: Deepseek API, requests library
- **Data Processing**: Python 3.x with JSON handling
- **Environment**: Conda virtual environment management
- **Browser**: Chrome WebDriver with automated driver management

## Project Structure

```
├── scripts/                 # Robot Framework test suites
│   ├── hkrt_content_scraper.robot      # Main scraping test
│   ├── hkrt_content_scraper_llm.robot  # Integrated scraping + analysis
│   └── hkrt_scraper.robot              # Basic scraper variant
├── resources/              # Python utilities and libraries
│   ├── deepseek_analyzer.py           # AI analysis module
│   └── example_usage.py               # Usage demonstration
├── results/                # Scraped data and analysis outputs
├── logs/                   # Test execution logs and reports
├── drivers/                # WebDriver binaries
├── requirements.txt        # Python dependencies
└── conda_env.bat          # Environment activation script
```

## Quick Start

### Prerequisites
- Python 3.8+
- Conda/Miniconda
- Chrome browser
- Deepseek API key

### Setup
1. **Clone and navigate**:
   ```bash
   cd robot_framework
   ```

2. **Create environment**:
   ```bash
   conda env create -f environment.yml  # or pip install -r requirements.txt
   ```

3. **Set API key**:
   ```bash
   export DEEPSEEK_API_KEY="your_api_key_here"
   ```

4. **Run the scraper**:
   ```bash
   conda activate robotframework
   robot --outputdir logs scripts/hkrt_content_scraper_llm.robot
   ```

### Usage Examples

**Basic Scraping**:
```bash
robot scripts/hkrt_content_scraper.robot
```

**AI Analysis**:
```python
from resources.deepseek_analyzer import DeepseekAnalyzer

analyzer = DeepseekAnalyzer()
result = analyzer.analyze_news("results/news_data.json")
```

## Output Formats

- **JSON Data**: Structured news extraction with title, date, and full content
- **Analysis Reports**: AI-generated insights with thematic summaries
- **Test Reports**: HTML/XML logs with execution details and screenshots

## Engineering Highlights

### Scalability & Reliability
- Configurable timeouts and retry mechanisms
- Memory-efficient data processing
- Error handling with graceful degradation
- Timestamped outputs preventing file conflicts

### Code Quality
- Modular architecture with clear separation of concerns
- Comprehensive documentation and logging
- Cross-platform compatibility
- Environment isolation with Conda

### Performance Optimization
- Headless browser execution for CI/CD compatibility
- Parallel processing capabilities
- Efficient API rate limiting
- Minimal resource footprint

## Applications

- **News Monitoring**: Automated content aggregation and analysis
- **Market Intelligence**: Real-time trend identification
- **Content Analysis**: AI-powered summarization and insights
- **Research Automation**: Systematic data collection workflows

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

This project showcases expertise in:
- Test automation frameworks
- Web scraping technologies
- API integration and authentication
- Data processing pipelines
- AI/LLM integration
- DevOps and CI/CD practices

For technical inquiries or collaboration opportunities, please review the codebase and execution logs.