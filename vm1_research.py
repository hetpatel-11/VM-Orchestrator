import os
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class ResearchVM:
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY')
        self.computer = Computer(project_id="yourcomputerid", api_key=self.api_key)
        print("🔍 Research VM (VM1) initialized!")
    
    def research_task(self, topic, depth="comprehensive"):
        """Perform research on a given topic"""
        print(f"🔍 Starting {depth} research on: {topic}")
        
        if depth == "quick":
            prompt = f"""
            Quick research task for {topic}:
            1. Open browser and search for {topic}
            2. Read the first 2-3 results
            3. Open text editor and write a brief summary (3-4 bullet points)
            4. Save as 'quick_research_{topic.replace(' ', '_')}.txt'
            """
        else:
            prompt = f"""
            Comprehensive research task for {topic}:
            1. Open browser and search for latest information about {topic}
            2. Visit 5-6 different authoritative websites
            3. Open another tab and search for recent news about {topic}
            4. Open text editor and create detailed research notes including:
               - Key facts and statistics
               - Recent developments 
               - Expert opinions
               - Future trends
            5. Save the comprehensive report as 'research_{topic.replace(' ', '_')}.txt'
            """
        
        self.computer.prompt(prompt)
        print(f"✅ Research on {topic} completed!")
    
    def competitive_analysis(self, industry):
        """Research competitors in an industry"""
        prompt = f"""
        Competitive analysis for {industry}:
        1. Search for top companies in {industry}
        2. Open websites of 3-4 major competitors
        3. Research their products, pricing, and market position
        4. Create a comparison document with findings
        5. Save as 'competitive_analysis_{industry.replace(' ', '_')}.txt'
        """
        
        self.computer.prompt(prompt)
        print(f"✅ Competitive analysis for {industry} completed!")
    
    def cleanup(self):
        self.computer.destroy()
        print("🧹 Research VM cleaned up!")

if __name__ == "__main__":
    vm = ResearchVM()
    try:
        # Example research tasks
        vm.research_task("blockchain technology", "comprehensive")
        # vm.competitive_analysis("electric vehicle market")
    finally:
        vm.cleanup() 
