import os
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class PresentationVM:
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY')
        self.computer = Computer(project_id="computer-2zaexgo", api_key=self.api_key)
        print("📊 Presentation VM (VM3) initialized!")
    
    def create_presentation(self, topic, style="professional"):
        """Create a comprehensive presentation"""
        print(f"📊 Creating {style} presentation for: {topic}")
        
        if style == "executive":
            prompt = f"""
            Executive presentation for {topic}:
            1. Open presentation software (Keynote, PowerPoint, or Google Slides)
            2. Create executive-level presentation with:
               - Title slide with executive summary
               - Market overview (1-2 slides)
               - Key insights and findings (2-3 slides)
               - Strategic recommendations (1-2 slides)
               - Financial implications (1 slide)
               - Next steps and timeline (1 slide)
            3. Use professional template with consistent branding
            4. Add high-quality charts and visuals
            5. Save as 'executive_{topic.replace(' ', '_')}.pptx'
            """
        else:
            prompt = f"""
            Professional presentation for {topic}:
            1. Open presentation software
            2. Create comprehensive presentation with:
               - Title slide with agenda
               - Introduction and background (2-3 slides)
               - Detailed analysis and data (4-5 slides)
               - Charts, graphs, and visualizations (3-4 slides)
               - Case studies or examples (2-3 slides)
               - Conclusions and recommendations (2-3 slides)
               - Q&A slide
            3. Use professional design with consistent formatting
            4. Add animations and transitions where appropriate
            5. Save as 'presentation_{topic.replace(' ', '_')}.pptx'
            """
        
        self.computer.prompt(prompt)
        print(f"✅ {style.title()} presentation for {topic} completed!")
    
    def create_dashboard(self, data_type):
        """Create visual dashboard"""
        prompt = f"""
        Dashboard creation for {data_type}:
        1. Open presentation software or design tool
        2. Create interactive dashboard with:
           - Key performance indicators (KPIs)
           - Real-time data visualizations
           - Trend analysis charts
           - Geographic data maps
           - Progress tracking meters
        3. Use dashboard template with modern design
        4. Add interactive elements and clear labels
        5. Save as 'dashboard_{data_type.replace(' ', '_')}.pptx'
        """
        
        self.computer.prompt(prompt)
        print(f"✅ Dashboard for {data_type} completed!")
    
    def create_report(self, report_type):
        """Create detailed report document"""
        prompt = f"""
        Report creation for {report_type}:
        1. Open word processor (Pages, Word, or Google Docs)
        2. Create professional report with:
           - Executive summary (1 page)
           - Table of contents
           - Introduction and methodology
           - Detailed findings with supporting data
           - Charts and tables embedded in text
           - Conclusions and recommendations
           - Appendices with additional data
        3. Format with professional styling and headers
        4. Add page numbers and consistent formatting
        5. Save as 'report_{report_type.replace(' ', '_')}.docx'
        """
        
        self.computer.prompt(prompt)
        print(f"✅ Report for {report_type} completed!")
    
    def create_infographic(self, topic):
        """Create visual infographic"""
        prompt = f"""
        Infographic creation for {topic}:
        1. Open design software or presentation tool
        2. Create visually appealing infographic with:
           - Eye-catching title and headers
           - Key statistics displayed prominently
           - Visual icons and graphics
           - Data flow charts or process diagrams
           - Color-coded sections for easy reading
        3. Use modern design principles with good visual hierarchy
        4. Ensure information is easy to digest at a glance
        5. Save as 'infographic_{topic.replace(' ', '_')}.png' and .pptx
        """
        
        self.computer.prompt(prompt)
        print(f"✅ Infographic for {topic} completed!")
    
    def cleanup(self):
        self.computer.destroy()
        print("🧹 Presentation VM cleaned up!")

if __name__ == "__main__":
    vm = PresentationVM()
    try:
        # Example presentation tasks
        vm.create_presentation("market analysis", "executive")
        # vm.create_dashboard("sales performance")
        # vm.create_report("quarterly review")
        # vm.create_infographic("industry trends")
    finally:
        vm.cleanup() 