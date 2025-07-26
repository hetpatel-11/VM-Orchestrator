import os
import time
import threading
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class VMOrchestrator:
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY')
        
        # Initialize all VMs
        self.vm1 = Computer(project_id="yourcomputerid", api_key=self.api_key)  # Research VM
        self.vm2 = Computer(project_id="yourcomputerid", api_key=self.api_key)  # Processing VM
        self.vm3 = Computer(project_id="yourcomputerid", api_key=self.api_key)  # Presentation VM
        
        print("🚀 All VMs initialized successfully!")
        
    def execute_distributed_task(self, topic="artificial intelligence trends"):
        """Execute a complex task across multiple VMs"""
        
        print(f"\n📋 Starting distributed research task on: {topic}")
        print("=" * 60)
        
        # Create threads for parallel execution
        threads = []
        
        # VM1: Research Task
        research_thread = threading.Thread(
            target=self.vm1_research_task, 
            args=(topic,)
        )
        
        # VM2: Data Processing Task  
        processing_thread = threading.Thread(
            target=self.vm2_processing_task, 
            args=(topic,)
        )
        
        # VM3: Presentation Task
        presentation_thread = threading.Thread(
            target=self.vm3_presentation_task, 
            args=(topic,)
        )
        
        # Start all tasks
        research_thread.start()
        time.sleep(5)  # Stagger the starts
        processing_thread.start()
        time.sleep(5)
        presentation_thread.start()
        
        # Wait for all to complete
        research_thread.join()
        processing_thread.join()
        presentation_thread.join()
        
        print("\n✅ All VMs completed their tasks!")
        
    def vm1_research_task(self, topic):
        """VM1: Research and data gathering"""
        print(f"🔍 VM1 (Research): Starting research on {topic}")
        
        prompt = f"""
        Open a browser and research {topic}. 
        1. Search for the latest news and articles about {topic}
        2. Open 3-4 relevant websites 
        3. Take notes in a text editor about key findings
        4. Save the research summary to a file called 'research_findings.txt'
        """
        
        self.vm1.prompt(prompt)
        print("🔍 VM1: Research task completed")
        
    def vm2_processing_task(self, topic):
        """VM2: Data processing and analysis"""
        print(f"⚙️ VM2 (Processing): Starting data processing for {topic}")
        
        prompt = f"""
        1. Open a spreadsheet application (Numbers or Excel)
        2. Create a comparison table analyzing different aspects of {topic}
        3. Add charts and graphs to visualize trends
        4. Calculate statistics and create a summary
        5. Export the analysis as 'data_analysis.csv'
        """
        
        self.vm2.prompt(prompt)
        print("⚙️ VM2: Processing task completed")
        
    def vm3_presentation_task(self, topic):
        """VM3: Create presentation and final output"""
        print(f"📊 VM3 (Presentation): Creating presentation for {topic}")
        
        prompt = f"""
        1. Open presentation software (Keynote or PowerPoint)
        2. Create a professional presentation about {topic}
        3. Include title slide, key findings, data visualization, and conclusions
        4. Add a slide with recommendations and future outlook
        5. Save the presentation as '{topic.replace(' ', '_')}_presentation.pptx'
        """
        
        self.vm3.prompt(prompt)
        print("📊 VM3: Presentation task completed")
        
    def cleanup(self):
        """Clean up all VM connections"""
        print("\n🧹 Cleaning up all VMs...")
        self.vm1.destroy()
        self.vm2.destroy() 
        self.vm3.destroy()
        print("✅ All VMs cleaned up successfully!")

def main():
    orchestrator = VMOrchestrator()
    
    try:
        # Example: Research AI trends across 3 VMs
        orchestrator.execute_distributed_task("artificial intelligence trends 2024")
        
        # You can add more complex workflows here
        # orchestrator.execute_distributed_task("renewable energy market analysis")
        
    finally:
        orchestrator.cleanup()

if __name__ == "__main__":
    main() 
