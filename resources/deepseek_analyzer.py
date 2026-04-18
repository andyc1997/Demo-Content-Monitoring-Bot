import json
import sys
import os
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests library not found. Install with: pip install requests")
    sys.exit(1)


class DeepseekAnalyzer:
    def __init__(self, api_key=None):
        """
        Initialize Deepseek analyzer
        
        Args:
            api_key: Deepseek API key (from environment variable if not provided)
        """
        self.api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise ValueError("DEEPSEEK_API_KEY environment variable or api_key parameter required")
        
        self.api_url = "https://api.deepseek.com/chat/completions"
        self.model = "deepseek-chat"
    
    def analyze_news(self, json_file_path, output_dir="results"):
        """
        Analyze news data from JSON file using Deepseek API
        
        Args:
            json_file_path: Path to JSON file with news data
            output_dir: Directory to save analysis results
            
        Returns:
            Path to output text file
        """
        # Read JSON file
        print(f"Reading JSON file: {json_file_path}")
        with open(json_file_path, 'r', encoding='utf-8') as f:
            news_data = json.load(f)
        
        # Prepare prompt
        prompt = self._prepare_prompt(news_data)
        
        # Call Deepseek API
        print("Sending request to Deepseek API...")
        analysis = self._call_deepseek_api(prompt)
        
        # Save results to text file
        output_file = self._save_analysis(analysis, output_dir, json_file_path)
        
        return output_file
    
    def _prepare_prompt(self, news_data):
        """Prepare prompt for Deepseek API"""
        news_text = ""
        for idx, item in enumerate(news_data, 1):
            news_text += f"\n--- News {idx} ---\n"
            news_text += f"Title: {item.get('title', 'N/A')}\n"
            news_text += f"Date: {item.get('date', 'N/A')}\n"
            news_text += f"Content: {item.get('content', 'N/A')}\n"
        
        prompt = f"""Please analyze the following news articles from Hong Kong (RTHK News). 
Provide a comprehensive analysis including:
1. Main themes and topics
2. Key events or developments
3. Summary of important information
4. Any patterns or trends observed

News Articles:
{news_text}

Please provide your analysis in a clear and structured format in English."""
        
        return prompt
    
    def _call_deepseek_api(self, prompt):
        """Call Deepseek API and return response"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful news analysis assistant. Analyze news content and provide structured insights."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 2000
        }
        
        try:
            response = requests.post(self.api_url, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            if "choices" in result and len(result["choices"]) > 0:
                return result["choices"][0]["message"]["content"]
            else:
                raise ValueError(f"Unexpected API response: {result}")
        
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"API request failed: {str(e)}")
    
    def _save_analysis(self, analysis, output_dir, json_file_path):
        """Save analysis to text file"""
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Generate output filename based on input JSON filename
        json_filename = Path(json_file_path).stem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = Path(output_dir) / f"{json_filename}_analysis_{timestamp}.txt"
        
        # Write analysis to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("DEEPSEEK NEWS ANALYSIS\n")
            f.write("=" * 80 + "\n")
            f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Source File: {json_file_path}\n")
            f.write("=" * 80 + "\n\n")
            f.write(analysis)
            f.write("\n\n" + "=" * 80 + "\n")
            f.write("End of Analysis\n")
            f.write("=" * 80 + "\n")
        
        print(f"Analysis saved to: {output_file}")
        return str(output_file)


def main():
    """Main entry point for the script"""
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <json_file_path> [api_key]")
        print(f"  json_file_path: Path to JSON file with news data")
        print(f"  api_key: Deepseek API key (optional, uses DEEPSEEK_API_KEY env var if not provided)")
        sys.exit(1)
    
    json_file = sys.argv[1]
    api_key = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        analyzer = DeepseekAnalyzer(api_key=api_key)
        output_file = analyzer.analyze_news(json_file)
        print(f"\nSuccess! Analysis saved to: {output_file}")
        return output_file
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
