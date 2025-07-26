import os
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class ProcessingVM:
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY')
        self.computer = Computer(project_id="computer-pum2j64p", api_key=self.api_key)
        print("⚙️ Processing VM (VM2) initialized!")
    
    def data_analysis_task(self, topic):
        """Analyze data and create visualizations"""
        print(f"⚙️ Starting data analysis for: {topic}")
        
        prompt = f"""
        Data analysis and visualization for {topic}:
        1. Open spreadsheet application (Numbers, Excel, or Google Sheets)
        2. Create a comprehensive data analysis with:
           - Market size data
           - Growth trends over time
           - Geographic distribution
           - Key performance metrics
        3. Add charts and graphs:
           - Bar charts for comparisons
           - Line graphs for trends
           - Pie charts for market share
        4. Create pivot tables for deeper analysis
        5. Export final analysis as 'analysis_{topic.replace(' ', '_')}.xlsx'
        """
        
        self.computer.prompt(prompt)
        print(f"✅ Data analysis for {topic} completed!")
    
    def financial_modeling(self, business_type):
        """Create financial models and projections"""
        prompt = f"""
        Financial modeling for {business_type}:
        1. Open spreadsheet application
        2. Create financial model including:
           - Revenue projections (3-year forecast)
           - Cost analysis
           - Profit & Loss statements
           - Cash flow projections
           - Break-even analysis
        3. Add sensitivity analysis with different scenarios
        4. Create charts showing financial trends
        5. Save as 'financial_model_{business_type.replace(' ', '_')}.xlsx'
        """
        
        self.computer.prompt(prompt)
        print(f"✅ Financial modeling for {business_type} completed!")
    
    def content_processing(self, content_type):
        """Process and organize content"""
        prompt = f"""
        Content processing for {content_type}:
        1. Open text editor or word processor
        2. Create structured content including:
           - Executive summary
           - Key findings organized by categories
           - Action items and recommendations
           - Timeline for implementation
        3. Format document professionally with headers and bullet points
        4. Create a separate summary document (1-page)
        5. Save both as 'processed_{content_type.replace(' ', '_')}.docx' and 'summary_{content_type.replace(' ', '_')}.docx'
        """
        
        self.computer.prompt(prompt)
        print(f"✅ Content processing for {content_type} completed!")
    
    def cleanup(self):
        self.computer.destroy()
        print("🧹 Processing VM cleaned up!")

if __name__ == "__main__":
    vm = ProcessingVM()
    try:
        # Example processing tasks
        vm.data_analysis_task("cryptocurrency market")
        # vm.financial_modeling("tech startup")
        # vm.content_processing("market research report")
    finally:
        vm.cleanup() 