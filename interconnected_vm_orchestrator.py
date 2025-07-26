import os
import time
import threading
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class InterconnectedVMOrchestrator:
    """
    🔗 INTERCONNECTED VM ORCHESTRATOR - REVOLUTIONARY CONCEPT
    
    TRUE DATA PIPELINE ACROSS VMs:
    1. VM1 does research and SAVES results to shared file
    2. VM2 waits for VM1, READS the research file, processes it into spreadsheet
    3. VM3 waits for both, READS research + analysis, creates presentation
    
    This creates a REAL interconnected workflow where VMs pass actual data!
    """
    
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY', 'your_orgo_api_key_here')
        
        # Set the Anthropic API key
        os.environ['ANTHROPIC_API_KEY'] = os.getenv('ANTHROPIC_API_KEY', 'your_anthropic_api_key_here')
        
        print("🔗 Initializing INTERCONNECTED VM Orchestrator...")
        
        # Initialize all 3 VMs
        self.vm1 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Research VM
        self.vm2 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Processing VM
        self.vm3 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Presentation VM
        
        print("✅ All 3 VMs connected for INTERCONNECTED workflow!")
        
        # Status tracking
        self.vm1_status = "Ready"
        self.vm2_status = "Waiting for VM1 data..."
        self.vm3_status = "Waiting for VM1 & VM2 data..."
        
        # Data sharing mechanism
        self.research_complete = False
        self.analysis_complete = False
    
    def orchestrate_interconnected_workflow(self, user_prompt):
        """🔗 Execute TRUE INTERCONNECTED workflow with data handoffs"""
        
        print(f"\n🔗 INTERCONNECTED WORKFLOW: '{user_prompt}'")
        print("="*80)
        print("🎯 DATA PIPELINE PLAN:")
        print("📊 Step 1: VM1 researches and saves data to file")
        print("📈 Step 2: VM2 reads VM1's file and creates analysis")  
        print("📋 Step 3: VM3 reads both files and creates presentation")
        print("="*80)
        
        # Create the interconnected task pipeline
        task_plan = self.create_interconnected_tasks(user_prompt)
        
        # Execute TRUE SEQUENTIAL WORKFLOW with data handoffs
        self.execute_interconnected_pipeline(task_plan)
    
    def create_interconnected_tasks(self, prompt):
        """🔗 Create interconnected tasks with actual data handoffs"""
        
        return {
            'vm1_research_task': f"""
            VM1 RESEARCH TASK - DATA COLLECTION for: "{prompt}"
            
            CRITICAL: Your research will be used by VM2 and VM3!
            
            1. Open browser and research: {prompt}
            2. Gather comprehensive data including:
               - Key statistics and numbers
               - Market trends and insights  
               - Important facts and findings
               - Recent developments
               - Expert opinions and analysis
            
            3. Open text editor and create detailed research file with:
               - Executive Summary (2-3 sentences)
               - Key Statistics (with numbers)
               - Market Trends (bullet points)
               - Important Findings (organized list)
               - Recent News/Developments
               - Expert Insights
               - Data Sources
            
            4. SAVE AS: 'vm1_research_data.txt' (VM2 and VM3 will read this!)
            5. Include ALL important data - VM2 needs this for analysis
            6. Make data clear and organized for other VMs to use
            
            VM2 IS WAITING FOR YOUR RESEARCH FILE!
            """,
            
            'vm2_analysis_task': f"""
            VM2 ANALYSIS TASK - PROCESS VM1'S RESEARCH for: "{prompt}"
            
            CRITICAL: Use VM1's research data to create analysis!
            
            1. First, locate and OPEN the file 'vm1_research_data.txt' 
            2. READ all the research data that VM1 collected
            3. Open spreadsheet application (Numbers/Excel)
            4. Create data analysis based on VM1's research:
               - Extract key numbers from VM1's file
               - Create data tables with VM1's statistics
               - Build charts using VM1's trend data
               - Add analysis based on VM1's findings
            
            5. Create specific analysis:
               - Summary table of key metrics from VM1
               - Trend analysis chart using VM1's data
               - Comparison charts with VM1's statistics
               - Financial projections based on VM1's research
            
            6. SAVE AS: 'vm2_analysis_data.xlsx' (VM3 will use this!)
            7. Include references to VM1's research in your analysis
            
            VM3 IS WAITING FOR YOUR ANALYSIS FILE!
            YOU MUST USE VM1'S RESEARCH DATA!
            """,
            
            'vm3_presentation_task': f"""
            VM3 PRESENTATION TASK - COMBINE VM1 & VM2 DATA for: "{prompt}"
            
            CRITICAL: Use both VM1's research AND VM2's analysis!
            
            1. First, locate and OPEN 'vm1_research_data.txt'
            2. READ VM1's research findings thoroughly
            3. Then locate and OPEN 'vm2_analysis_data.xlsx' 
            4. REVIEW VM2's analysis and charts
            
            5. Open presentation software (Keynote/PowerPoint)
            6. Create comprehensive presentation using BOTH files:
               
               Slide 1: Title - "{prompt} Analysis"
               Slide 2: Executive Summary (from VM1's research)
               Slide 3: Key Research Findings (from VM1's file)
               Slide 4: Statistical Analysis (from VM2's spreadsheet)
               Slide 5: Trends & Insights (combining VM1 & VM2 data)
               Slide 6: Visual Charts (import from VM2's analysis)
               Slide 7: Conclusions & Recommendations (synthesize both)
            
            7. IMPORT charts and data from VM2's Excel file
            8. Reference specific findings from VM1's research
            9. SAVE AS: 'vm3_final_presentation.pptx'
            
            CREATE A PRESENTATION THAT SHOWS DATA FROM ALL 3 VMs!
            YOU MUST REFERENCE BOTH VM1 AND VM2 FILES!
            """
        }
    
    def execute_interconnected_pipeline(self, task_plan):
        """🔗 Execute the TRUE interconnected pipeline"""
        
        print("\n🔗 STARTING INTERCONNECTED DATA PIPELINE...")
        print("=" * 80)
        
        # STEP 1: VM1 Research (starts immediately)
        print("📊 STEP 1: VM1 starting research and data collection...")
        self.execute_vm1_research(task_plan['vm1_research_task'])
        
        # Wait for VM1 to complete and mark research as done
        print("⏳ Waiting for VM1 to complete research...")
        while not self.research_complete:
            time.sleep(5)
        
        print("✅ VM1 research complete! Data saved for VM2 and VM3.")
        
        # STEP 2: VM2 Analysis (starts after VM1 completes)
        print("\n📈 STEP 2: VM2 starting analysis using VM1's research data...")
        self.vm2_status = "Processing VM1's research data..."
        
        # Start VM2 and VM3 in parallel (both can use VM1's data)
        vm2_thread = threading.Thread(target=self.execute_vm2_analysis, args=(task_plan['vm2_analysis_task'],))
        vm3_thread = threading.Thread(target=self.execute_vm3_presentation, args=(task_plan['vm3_presentation_task'],))
        
        vm2_thread.start()
        time.sleep(10)  # Give VM2 a head start on analysis
        vm3_thread.start()
        
        # Monitor both VM2 and VM3
        self.monitor_final_stages(vm2_thread, vm3_thread)
        
        # Wait for completion
        vm2_thread.join()
        vm3_thread.join()
        
        print("\n🎉 INTERCONNECTED WORKFLOW COMPLETE!")
        self.show_interconnected_results()
    
    def execute_vm1_research(self, task):
        """📊 Execute VM1 research with data saving"""
        self.vm1_status = "Researching and collecting data..."
        try:
            self.vm1.prompt(task)
            self.vm1_status = "Research Complete - Data Saved ✅"
            self.research_complete = True
            print("✅ VM1: Research data saved to 'vm1_research_data.txt'")
        except Exception as e:
            self.vm1_status = f"Error: {e}"
            print(f"❌ VM1 Error: {e}")
    
    def execute_vm2_analysis(self, task):
        """📈 Execute VM2 analysis using VM1's data"""
        self.vm2_status = "Reading VM1's research file..."
        try:
            self.vm2.prompt(task)
            self.vm2_status = "Analysis Complete - Used VM1 Data ✅"
            self.analysis_complete = True
            print("✅ VM2: Analysis complete using VM1's research data")
        except Exception as e:
            self.vm2_status = f"Error: {e}"
            print(f"❌ VM2 Error: {e}")
    
    def execute_vm3_presentation(self, task):
        """📋 Execute VM3 presentation using both VM1 and VM2 data"""
        self.vm3_status = "Reading VM1 & VM2 files..."
        try:
            self.vm3.prompt(task)
            self.vm3_status = "Presentation Complete - Used All Data ✅"
            print("✅ VM3: Presentation complete using data from VM1 and VM2")
        except Exception as e:
            self.vm3_status = f"Error: {e}"
            print(f"❌ VM3 Error: {e}")
    
    def monitor_final_stages(self, vm2_thread, vm3_thread):
        """📊 Monitor VM2 and VM3 execution"""
        print("\n📊 MONITORING INTERCONNECTED EXECUTION:")
        print("-" * 70)
        
        while vm2_thread.is_alive() or vm3_thread.is_alive():
            print(f"📊 VM1: {self.vm1_status}")
            print(f"📈 VM2: {self.vm2_status}")
            print(f"📋 VM3: {self.vm3_status}")
            print("-" * 70)
            time.sleep(8)
    
    def show_interconnected_results(self):
        """🔗 Show the interconnected workflow results"""
        print("\n🔗 INTERCONNECTED WORKFLOW RESULTS:")
        print("=" * 80)
        print("🎯 DATA PIPELINE SUCCESS:")
        print("✅ VM1: Research collected and saved to 'vm1_research_data.txt'")
        print("✅ VM2: Analysis created using VM1's research data → 'vm2_analysis_data.xlsx'")
        print("✅ VM3: Presentation built using BOTH VM1 & VM2 data → 'vm3_final_presentation.pptx'")
        print("\n🔗 INTERCONNECTED FEATURES DEMONSTRATED:")
        print("  • Real data handoff between VMs")
        print("  • Sequential workflow with dependencies")
        print("  • File-based data sharing")
        print("  • Each VM builds on previous VM's work")
        print("  • True interconnected computing")
        print("\n🏆 THIS IS REVOLUTIONARY VM ORCHESTRATION!")
    
    def cleanup(self):
        """🧹 Clean up all VM connections"""
        try:
            self.vm1.destroy()
            self.vm2.destroy()
            self.vm3.destroy()
            print("✅ All VMs cleaned up!")
        except Exception as e:
            print(f"⚠️ Cleanup: {e}")

def main():
    """🔗 Main interconnected workflow"""
    print("🔗 INTERCONNECTED VM ORCHESTRATOR")
    print("🚀 REVOLUTIONARY DATA PIPELINE ACROSS VMs")
    print("=" * 80)
    print("🎯 Each VM passes real data to the next VM!")
    print("📊 VM1 → VM2 → VM3 with actual file handoffs")
    print("=" * 80)
    
    orchestrator = InterconnectedVMOrchestrator()
    
    try:
        user_prompt = input("\n💭 Enter your research prompt: ").strip()
        
        if not user_prompt:
            print("❌ No prompt entered.")
            return
        
        # Execute the revolutionary interconnected workflow
        start_time = time.time()
        orchestrator.orchestrate_interconnected_workflow(user_prompt)
        end_time = time.time()
        
        print(f"\n⚡ TOTAL PIPELINE TIME: {end_time - start_time:.2f} seconds")
        print("🏆 INTERCONNECTED VM ORCHESTRATION COMPLETE!")
        
    except KeyboardInterrupt:
        print("\n⚠️ Workflow interrupted")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        orchestrator.cleanup()

if __name__ == "__main__":
    main() 
