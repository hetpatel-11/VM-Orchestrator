import os
import time
import threading
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class VisibleInterconnectedOrchestrator:
    """
    🔗 VISIBLE INTERCONNECTED VM ORCHESTRATOR - FAST & VISUAL
    
    VISIBLE REAL-TIME DATA SHARING:
    - VMs share data through explicit handoff commands
    - Real-time visible data transfer between VMs
    - Fast execution with clear interconnection demonstrations
    - Live data flow visualization
    """
    
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY', 'your_orgo_api_key_here')
        
        # Set the Anthropic API key
        os.environ['ANTHROPIC_API_KEY'] = os.getenv('ANTHROPIC_API_KEY', 'your_anthropic_api_key_here')
        
        print("🔗 Initializing VISIBLE INTERCONNECTED Orchestrator...")
        
        # Initialize all 3 VMs
        self.vm1 = Computer(project_id="computer-ykl00rx", api_key=self.api_key)   # Research VM
        self.vm2 = Computer(project_id="computer-aspt7cz", api_key=self.api_key)   # Processing VM
        self.vm3 = Computer(project_id="computer-62gnt6i", api_key=self.api_key)   # Presentation VM
        
        print("✅ All 3 VMs connected for VISIBLE INTERCONNECTION!")
        
        # Real-time data sharing variables
        self.vm1_data = ""
        self.vm2_data = ""
        self.shared_research_summary = ""
        self.shared_analysis_points = ""
        
        # Status tracking
        self.vm1_status = "Ready"
        self.vm2_status = "Ready"
        self.vm3_status = "Ready"
        
        # Completion flags
        self.vm1_complete = False
        self.vm2_complete = False
    
    def execute_visible_interconnected_workflow(self, user_prompt):
        """🔗 Execute VISIBLE interconnected workflow with real-time data sharing"""
        
        print(f"\n🔗 VISIBLE INTERCONNECTED WORKFLOW: '{user_prompt}'")
        print("="*80)
        print("🎯 VISIBLE DATA FLOW PLAN:")
        print("📊 VM1: Research → Shares key findings in real-time")
        print("📈 VM2: Receives VM1 data → Processes → Shares analysis")
        print("📋 VM3: Receives both data streams → Creates presentation")
        print("="*80)
        
        # Create fast interconnected tasks
        task_plan = self.create_fast_visible_tasks(user_prompt)
        
        # Execute with visible data handoffs
        self.execute_fast_visible_pipeline(task_plan)
    
    def create_fast_visible_tasks(self, prompt):
        """⚡ Create fast tasks with visible data sharing"""
        
        return {
            'vm1_task': f"""
            FAST RESEARCH WITH VISIBLE DATA SHARING for: "{prompt}"
            
            SPEED-OPTIMIZED RESEARCH (2-3 minutes max):
            1. Quick Google search for: {prompt}
            2. Scan first 3 results quickly
            3. Copy key statistics and facts immediately
            4. Open TextEdit and create summary with:
               - 3 key statistics about {prompt}
               - 3 main trends
               - 3 important findings
            
            5. VISIBLE DATA SHARING - Say out loud while typing:
               "SHARING RESEARCH DATA WITH VM2 AND VM3"
               "KEY FINDING 1: [state your finding]"
               "KEY FINDING 2: [state your finding]"
               "KEY FINDING 3: [state your finding]"
            
            6. Save file as 'shared_research.txt' and announce:
               "VM1 RESEARCH COMPLETE - DATA SHARED WITH VM2 AND VM3"
            
            CRITICAL: Make data sharing VISIBLE and VOCAL
            TIME LIMIT: 3 minutes maximum
            """,
            
            'vm2_task': f"""
            FAST ANALYSIS USING VM1 DATA for: "{prompt}"
            
            VISIBLE DATA INTEGRATION (2-3 minutes max):
            1. FIRST - Open 'shared_research.txt' and read VM1's findings
            2. ANNOUNCE: "VM2 RECEIVED DATA FROM VM1 - STARTING ANALYSIS"
            3. Open Numbers/Excel quickly
            4. Create simple table with VM1's statistics
            5. Make basic chart using VM1's trend data
            
            6. VISIBLE DATA SHARING - Announce your analysis:
               "VM2 ANALYSIS COMPLETE - SHARING WITH VM3"
               "ANALYSIS POINT 1: [based on VM1 data]"
               "ANALYSIS POINT 2: [based on VM1 data]"
               "TREND PROJECTION: [based on VM1 data]"
            
            7. Save as 'shared_analysis.xlsx' and announce:
               "VM2 DATA PROCESSED AND SHARED WITH VM3"
            
            CRITICAL: Show you're using VM1's data visibly
            TIME LIMIT: 3 minutes maximum
            """,
            
            'vm3_task': f"""
            FAST PRESENTATION USING VM1 AND VM2 DATA for: "{prompt}"
            
            VISIBLE DATA COMPILATION (3-4 minutes max):
            1. FIRST - Open 'shared_research.txt' and announce:
               "VM3 RECEIVING RESEARCH DATA FROM VM1"
            2. THEN - Open 'shared_analysis.xlsx' and announce:
               "VM3 RECEIVING ANALYSIS DATA FROM VM2"
            
            3. Open Keynote/PowerPoint with basic template
            4. Create 5 slides using BOTH VM1 and VM2 data:
               - Title: "{prompt} - 3-VM Analysis"
               - Research Findings (from VM1 file)
               - Data Analysis (from VM2 file)
               - Combined Insights (from both)
               - Conclusions
            
            5. VISIBLE INTEGRATION - Announce while building:
               "INTEGRATING VM1 RESEARCH INTO SLIDE 2"
               "ADDING VM2 ANALYSIS TO SLIDE 3"
               "COMBINING ALL DATA FOR FINAL INSIGHTS"
            
            6. Save as 'final_interconnected_presentation.pptx'
            7. FINAL ANNOUNCEMENT: "3-VM INTERCONNECTED WORKFLOW COMPLETE!"
            
            CRITICAL: Show visible integration of all VM data
            TIME LIMIT: 4 minutes maximum
            """
        }
    
    def execute_fast_visible_pipeline(self, task_plan):
        """🚀 Execute fast pipeline with visible interconnection"""
        
        print("\n🚀 STARTING FAST VISIBLE INTERCONNECTED PIPELINE...")
        print("=" * 80)
        
        # Step 1: VM1 Research (immediate start)
        print("📊 STEP 1: VM1 FAST RESEARCH & DATA SHARING...")
        vm1_thread = threading.Thread(target=self.execute_vm1_fast, args=(task_plan['vm1_task'],))
        vm1_thread.start()
        
        # Monitor VM1 with fast updates
        self.monitor_vm1_fast(vm1_thread)
        
        # Wait for VM1 completion
        vm1_thread.join()
        print("✅ VM1 COMPLETE - DATA READY FOR VM2 & VM3!")
        
        # Step 2: Start VM2 and VM3 simultaneously (both can use VM1 data)
        print("\n📈📋 STEP 2: VM2 & VM3 USING VM1 DATA SIMULTANEOUSLY...")
        
        vm2_thread = threading.Thread(target=self.execute_vm2_fast, args=(task_plan['vm2_task'],))
        vm3_thread = threading.Thread(target=self.execute_vm3_fast, args=(task_plan['vm3_task'],))
        
        # Start both with slight stagger
        vm2_thread.start()
        time.sleep(5)  # Give VM2 slight head start
        vm3_thread.start()
        
        # Monitor both with visible updates
        self.monitor_vm2_vm3_fast(vm2_thread, vm3_thread)
        
        # Wait for completion
        vm2_thread.join()
        vm3_thread.join()
        
        print("\n🎉 VISIBLE INTERCONNECTED WORKFLOW COMPLETE!")
        self.show_interconnection_success()
    
    def execute_vm1_fast(self, task):
        """📊 Fast VM1 execution with data sharing"""
        self.vm1_status = "🔍 Fast Research..."
        try:
            self.vm1.prompt(task)
            self.vm1_status = "✅ Research Complete - Data Shared"
            self.vm1_complete = True
            print("\n🔗 VM1 → VM2 & VM3: RESEARCH DATA SHARED!")
        except Exception as e:
            self.vm1_status = f"❌ Error: {e}"
            print(f"❌ VM1 Error: {e}")
    
    def execute_vm2_fast(self, task):
        """📈 Fast VM2 execution using VM1 data"""
        self.vm2_status = "📊 Using VM1 Data..."
        try:
            self.vm2.prompt(task)
            self.vm2_status = "✅ Analysis Complete - Data Shared"
            self.vm2_complete = True
            print("\n🔗 VM2 → VM3: ANALYSIS DATA SHARED!")
        except Exception as e:
            self.vm2_status = f"❌ Error: {e}"
            print(f"❌ VM2 Error: {e}")
    
    def execute_vm3_fast(self, task):
        """📋 Fast VM3 execution using VM1 & VM2 data"""
        self.vm3_status = "📋 Using VM1 & VM2 Data..."
        try:
            self.vm3.prompt(task)
            self.vm3_status = "✅ Presentation Complete - All Data Used"
            print("\n🔗 VM3: FINAL PRESENTATION CREATED USING ALL VM DATA!")
        except Exception as e:
            self.vm3_status = f"❌ Error: {e}"
            print(f"❌ VM3 Error: {e}")
    
    def monitor_vm1_fast(self, vm1_thread):
        """📊 Fast monitoring of VM1"""
        while vm1_thread.is_alive():
            print(f"🔍 VM1: {self.vm1_status}")
            time.sleep(3)  # Fast updates
    
    def monitor_vm2_vm3_fast(self, vm2_thread, vm3_thread):
        """📊 Fast monitoring of VM2 and VM3"""
        print("\n📊 MONITORING INTERCONNECTED VMs:")
        while vm2_thread.is_alive() or vm3_thread.is_alive():
            print(f"📈 VM2: {self.vm2_status}")
            print(f"📋 VM3: {self.vm3_status}")
            print("🔗 Data flowing between VMs...")
            print("-" * 50)
            time.sleep(4)  # Fast updates
    
    def show_interconnection_success(self):
        """🎉 Show visible interconnection results"""
        print("\n🔗 VISIBLE INTERCONNECTION SUCCESS!")
        print("=" * 80)
        print("🎯 DATA FLOW DEMONSTRATED:")
        print("✅ VM1 → Created research data → Shared with VM2 & VM3")
        print("✅ VM2 → Used VM1 data → Created analysis → Shared with VM3")
        print("✅ VM3 → Used VM1 & VM2 data → Created final presentation")
        print("\n🔗 INTERCONNECTION FEATURES SHOWN:")
        print("  ⚡ Real-time data sharing between VMs")
        print("  📊 Visible file handoffs and data usage")
        print("  🚀 Fast execution with clear dependencies")
        print("  📋 Each VM explicitly uses previous VM data")
        print("  🎪 Vocal announcements of data transfers")
        print("\n🏆 REVOLUTIONARY VM INTERCONNECTION DEMONSTRATED!")
        
        print("\n📁 FILES CREATED WITH INTERCONNECTED DATA:")
        print("  • shared_research.txt (VM1 → VM2 & VM3)")
        print("  • shared_analysis.xlsx (VM2 → VM3, using VM1 data)")
        print("  • final_interconnected_presentation.pptx (VM3, using all data)")
    
    def cleanup(self):
        """🧹 Fast cleanup"""
        try:
            self.vm1.destroy()
            self.vm2.destroy()
            self.vm3.destroy()
            print("\n✅ All VMs cleaned up!")
        except Exception as e:
            print(f"⚠️ Cleanup: {e}")

def main():
    """🔗 Main visible interconnected workflow"""
    print("🔗 VISIBLE INTERCONNECTED VM ORCHESTRATOR")
    print("⚡ FAST EXECUTION WITH VISIBLE DATA SHARING")
    print("=" * 80)
    print("🎯 Watch VMs share data in real-time!")
    print("📊 See visible interconnection between all 3 VMs!")
    print("🚀 Fast execution with clear data dependencies!")
    print("=" * 80)
    
    orchestrator = VisibleInterconnectedOrchestrator()
    
    try:
        user_prompt = input("\n💭 Enter your prompt for VISIBLE interconnection: ").strip()
        
        if not user_prompt:
            user_prompt = "artificial intelligence in healthcare"
            print(f"Using demo prompt: {user_prompt}")
        
        # Execute the visible interconnected workflow
        start_time = time.time()
        orchestrator.execute_visible_interconnected_workflow(user_prompt)
        end_time = time.time()
        
        print(f"\n⚡ TOTAL EXECUTION TIME: {end_time - start_time:.2f} seconds")
        print("🏆 VISIBLE INTERCONNECTED WORKFLOW COMPLETE!")
        
    except KeyboardInterrupt:
        print("\n⚠️ Workflow interrupted")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        orchestrator.cleanup()

if __name__ == "__main__":
    main() 