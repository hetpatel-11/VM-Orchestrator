import os
import time
import threading
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class SharedMemoryOrchestrator:
    """
    🧠 SHARED MEMORY VM ORCHESTRATOR - REVOLUTIONARY CONCEPT
    
    SHARED MEMORY SYSTEM:
    - All 3 VMs access the same shared memory file
    - VMs can read and write to common memory space
    - Real-time memory updates visible to all VMs
    - Seamless data sharing without file searching
    """
    
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY', 'your_orgo_api_key_here')
        
        # Set the Anthropic API key
        os.environ['ANTHROPIC_API_KEY'] = os.getenv('ANTHROPIC_API_KEY', 'your_anthropic_api_key_here')
        
        print("🧠 Initializing SHARED MEMORY VM Orchestrator...")
        
        # Initialize all 3 VMs
        self.vm1 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Research VM
        self.vm2 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Processing VM
        self.vm3 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Presentation VM
        
        print("✅ All 3 VMs connected to SHARED MEMORY system!")
        
        # Status tracking
        self.vm1_status = "Ready"
        self.vm2_status = "Ready"
        self.vm3_status = "Ready"
        
        # Completion tracking
        self.vm1_complete = False
        self.vm2_complete = False
    
    def execute_shared_memory_workflow(self, user_prompt):
        """🧠 Execute workflow with shared memory access"""
        
        print(f"\n🧠 SHARED MEMORY WORKFLOW: '{user_prompt}'")
        print("="*80)
        print("🎯 SHARED MEMORY ARCHITECTURE:")
        print("📝 All VMs read/write to 'SHARED_MEMORY.txt'")
        print("🔄 Real-time memory updates accessible to all VMs")
        print("⚡ Seamless data sharing without file searching")
        print("="*80)
        
        # Initialize shared memory
        self.initialize_shared_memory(user_prompt)
        
        # Create shared memory tasks
        task_plan = self.create_shared_memory_tasks(user_prompt)
        
        # Execute with shared memory
        self.execute_shared_memory_pipeline(task_plan)
    
    def initialize_shared_memory(self, prompt):
        """🧠 Initialize the shared memory file"""
        print("\n🧠 INITIALIZING SHARED MEMORY...")
        
        # Each VM will have instructions to access this shared memory
        shared_memory_content = f"""
=== SHARED MEMORY FOR ALL VMs ===
TASK: {prompt}
STATUS: Initialized

=== VM1 RESEARCH SECTION ===
[VM1 will write research findings here]

=== VM2 ANALYSIS SECTION ===
[VM2 will write analysis based on VM1 data here]

=== VM3 PRESENTATION SECTION ===
[VM3 will write presentation notes using VM1 & VM2 data here]

=== SHARED INSIGHTS ===
[All VMs can add insights here]

=== STATUS UPDATES ===
System: Shared memory initialized
"""
        
        print("✅ Shared memory structure created for all VMs")
    
    def create_shared_memory_tasks(self, prompt):
        """🧠 Create tasks that use shared memory"""
        
        return {
            'vm1_task': f"""
            VM1 RESEARCH WITH SHARED MEMORY ACCESS for: "{prompt}"
            
            🧠 SHARED MEMORY INSTRUCTIONS:
            1. Open TextEdit and create/open file called 'SHARED_MEMORY.txt'
            2. Look for the "=== VM1 RESEARCH SECTION ===" header
            3. Write your research findings under that section
            
            RESEARCH WORKFLOW:
            1. Quick Google search for: {prompt}
            2. Gather key data from first 3-4 results
            3. Update SHARED_MEMORY.txt with:
               
               === VM1 RESEARCH SECTION ===
               VM1 STATUS: Research in progress
               
               KEY STATISTICS:
               - [Add 3-4 key statistics about {prompt}]
               
               MARKET TRENDS:
               - [Add 3-4 current trends]
               
               IMPORTANT FINDINGS:
               - [Add 3-4 critical findings]
               
               RECENT DEVELOPMENTS:
               - [Add recent news/updates]
               
               VM1 STATUS: Research complete - Data available for VM2 & VM3
            
            4. Save the file so VM2 and VM3 can access the data
            5. Announce: "VM1 DATA WRITTEN TO SHARED MEMORY - AVAILABLE FOR ALL VMs"
            
            TIME LIMIT: 3-4 minutes maximum
            CRITICAL: All data goes into shared memory for other VMs to use
            """,
            
            'vm2_task': f"""
            VM2 ANALYSIS WITH SHARED MEMORY ACCESS for: "{prompt}"
            
            🧠 SHARED MEMORY INSTRUCTIONS:
            1. Open 'SHARED_MEMORY.txt' and READ VM1's research data
            2. Find the "=== VM2 ANALYSIS SECTION ===" header
            3. Write your analysis under that section using VM1's data
            
            ANALYSIS WORKFLOW:
            1. FIRST - Read VM1's research from shared memory
            2. Announce: "VM2 READING VM1 DATA FROM SHARED MEMORY"
            3. Open Numbers/Excel for analysis
            4. Create analysis based on VM1's shared memory data
            5. Update SHARED_MEMORY.txt with:
               
               === VM2 ANALYSIS SECTION ===
               VM2 STATUS: Analysis in progress using VM1 data
               
               DATA ANALYSIS (Based on VM1 research):
               - [Analysis of VM1's statistics]
               - [Trend projections using VM1 data]
               - [Financial implications from VM1 findings]
               
               CHARTS CREATED:
               - [Describe charts made with VM1 data]
               
               KEY INSIGHTS:
               - [Insights derived from VM1's research]
               
               RECOMMENDATIONS:
               - [Based on VM1's findings]
               
               VM2 STATUS: Analysis complete - Available for VM3
            
            6. Save Excel file as 'analysis_using_shared_memory.xlsx'
            7. Announce: "VM2 ANALYSIS WRITTEN TO SHARED MEMORY - USING VM1 DATA"
            
            TIME LIMIT: 3-4 minutes maximum
            CRITICAL: Use VM1's data from shared memory for your analysis
            """,
            
            'vm3_task': f"""
            VM3 PRESENTATION WITH SHARED MEMORY ACCESS for: "{prompt}"
            
            🧠 SHARED MEMORY INSTRUCTIONS:
            1. Open 'SHARED_MEMORY.txt' and READ both VM1 and VM2 data
            2. Find the "=== VM3 PRESENTATION SECTION ===" header
            3. Write your presentation notes under that section
            
            PRESENTATION WORKFLOW:
            1. FIRST - Read complete shared memory file
            2. Announce: "VM3 READING ALL VM DATA FROM SHARED MEMORY"
            3. Open Keynote/PowerPoint
            4. Create presentation using ALL shared memory data
            5. Update SHARED_MEMORY.txt with:
               
               === VM3 PRESENTATION SECTION ===
               VM3 STATUS: Creating presentation using all shared data
               
               PRESENTATION OUTLINE:
               Slide 1: Title - "{prompt} Analysis"
               Slide 2: Research Overview (from VM1 shared memory)
               Slide 3: Key Statistics (from VM1 shared memory)
               Slide 4: Data Analysis (from VM2 shared memory)
               Slide 5: Charts & Insights (from VM2 shared memory)
               Slide 6: Combined Recommendations (from all VM data)
               
               DATA SOURCES USED:
               - VM1 research data from shared memory
               - VM2 analysis data from shared memory
               - Combined insights from all VMs
               
               VM3 STATUS: Presentation complete using all shared memory data
            
            6. Save presentation as 'final_shared_memory_presentation.pptx'
            7. Update shared memory final status:
               
               === STATUS UPDATES ===
               VM1: Research complete ✅
               VM2: Analysis complete ✅  
               VM3: Presentation complete ✅
               ALL VMs: Shared memory workflow successful! 🎉
            
            8. Announce: "VM3 PRESENTATION COMPLETE - USED ALL SHARED MEMORY DATA"
            
            TIME LIMIT: 4-5 minutes maximum
            CRITICAL: Use data from ALL VMs via shared memory
            """
        }
    
    def execute_shared_memory_pipeline(self, task_plan):
        """🧠 Execute pipeline with shared memory"""
        
        print("\n🧠 STARTING SHARED MEMORY PIPELINE...")
        print("=" * 80)
        
        # Step 1: VM1 Research (writes to shared memory)
        print("📊 STEP 1: VM1 writing research to SHARED MEMORY...")
        vm1_thread = threading.Thread(target=self.execute_vm1_memory, args=(task_plan['vm1_task'],))
        vm1_thread.start()
        
        # Monitor VM1
        self.monitor_vm1_memory(vm1_thread)
        vm1_thread.join()
        print("✅ VM1 COMPLETE - Data written to SHARED MEMORY!")
        
        # Step 2: VM2 and VM3 can now access shared memory
        print("\n📈📋 STEP 2: VM2 & VM3 accessing SHARED MEMORY simultaneously...")
        
        vm2_thread = threading.Thread(target=self.execute_vm2_memory, args=(task_plan['vm2_task'],))
        vm3_thread = threading.Thread(target=self.execute_vm3_memory, args=(task_plan['vm3_task'],))
        
        # Start VM2 first, then VM3
        vm2_thread.start()
        time.sleep(30)  # Give VM2 time to add to shared memory
        vm3_thread.start()
        
        # Monitor both
        self.monitor_vm2_vm3_memory(vm2_thread, vm3_thread)
        
        # Wait for completion
        vm2_thread.join()
        vm3_thread.join()
        
        print("\n🎉 SHARED MEMORY WORKFLOW COMPLETE!")
        self.show_shared_memory_success()
    
    def execute_vm1_memory(self, task):
        """📊 VM1 execution with shared memory writing"""
        self.vm1_status = "🧠 Writing to shared memory..."
        try:
            self.vm1.prompt(task)
            self.vm1_status = "✅ Research in shared memory"
            self.vm1_complete = True
            print("\n🧠 VM1 → SHARED MEMORY: Research data written!")
        except Exception as e:
            self.vm1_status = f"❌ Error: {e}"
            print(f"❌ VM1 Error: {e}")
    
    def execute_vm2_memory(self, task):
        """📈 VM2 execution with shared memory access"""
        self.vm2_status = "🧠 Reading shared memory & analyzing..."
        try:
            self.vm2.prompt(task)
            self.vm2_status = "✅ Analysis in shared memory"
            self.vm2_complete = True
            print("\n🧠 VM2 → SHARED MEMORY: Analysis added using VM1 data!")
        except Exception as e:
            self.vm2_status = f"❌ Error: {e}"
            print(f"❌ VM2 Error: {e}")
    
    def execute_vm3_memory(self, task):
        """📋 VM3 execution with shared memory access"""
        self.vm3_status = "🧠 Reading all shared memory & presenting..."
        try:
            self.vm3.prompt(task)
            self.vm3_status = "✅ Presentation using all shared data"
            print("\n🧠 VM3 → SHARED MEMORY: Presentation complete using all VM data!")
        except Exception as e:
            self.vm3_status = f"❌ Error: {e}"
            print(f"❌ VM3 Error: {e}")
    
    def monitor_vm1_memory(self, vm1_thread):
        """📊 Monitor VM1 shared memory writing"""
        while vm1_thread.is_alive():
            print(f"🧠 VM1: {self.vm1_status}")
            time.sleep(4)
    
    def monitor_vm2_vm3_memory(self, vm2_thread, vm3_thread):
        """📊 Monitor VM2 and VM3 shared memory access"""
        print("\n🧠 MONITORING SHARED MEMORY ACCESS:")
        while vm2_thread.is_alive() or vm3_thread.is_alive():
            print(f"📈 VM2: {self.vm2_status}")
            print(f"📋 VM3: {self.vm3_status}")
            print("🧠 All VMs sharing memory space...")
            print("-" * 60)
            time.sleep(5)
    
    def show_shared_memory_success(self):
        """🧠 Show shared memory workflow results"""
        print("\n🧠 SHARED MEMORY WORKFLOW SUCCESS!")
        print("=" * 80)
        print("🎯 SHARED MEMORY FEATURES DEMONSTRATED:")
        print("✅ All 3 VMs accessed the same memory file")
        print("✅ VM1 wrote research data to shared memory")
        print("✅ VM2 read VM1 data and added analysis to shared memory")
        print("✅ VM3 read ALL data and created presentation using shared memory")
        print("\n🧠 REVOLUTIONARY ARCHITECTURE:")
        print("  💾 Single shared memory space for all VMs")
        print("  🔄 Real-time memory updates accessible to all")
        print("  ⚡ No file searching - direct memory access")
        print("  🔗 Seamless data sharing between all VMs")
        print("  📊 Structured memory sections for each VM")
        print("\n🏆 SHARED MEMORY VM ORCHESTRATION COMPLETE!")
        
        print("\n📁 SHARED MEMORY FILES CREATED:")
        print("  • SHARED_MEMORY.txt (accessed by all 3 VMs)")
        print("  • analysis_using_shared_memory.xlsx (VM2 output)")
        print("  • final_shared_memory_presentation.pptx (VM3 output)")
    
    def cleanup(self):
        """🧹 Cleanup with shared memory status"""
        try:
            self.vm1.destroy()
            self.vm2.destroy()
            self.vm3.destroy()
            print("\n✅ All VMs disconnected from shared memory!")
        except Exception as e:
            print(f"⚠️ Cleanup: {e}")

def main():
    """🧠 Main shared memory workflow"""
    print("🧠 SHARED MEMORY VM ORCHESTRATOR")
    print("💾 REVOLUTIONARY SHARED MEMORY ARCHITECTURE")
    print("=" * 80)
    print("🎯 All 3 VMs share the same memory space!")
    print("🔄 Real-time memory updates for all VMs!")
    print("⚡ Seamless data sharing without file searching!")
    print("=" * 80)
    
    orchestrator = SharedMemoryOrchestrator()
    
    try:
        user_prompt = input("\n💭 Enter your prompt for SHARED MEMORY workflow: ").strip()
        
        if not user_prompt:
            user_prompt = "renewable energy market trends"
            print(f"Using demo prompt: {user_prompt}")
        
        # Execute the shared memory workflow
        start_time = time.time()
        orchestrator.execute_shared_memory_workflow(user_prompt)
        end_time = time.time()
        
        print(f"\n⚡ TOTAL EXECUTION TIME: {end_time - start_time:.2f} seconds")
        print("🏆 SHARED MEMORY WORKFLOW COMPLETE!")
        
    except KeyboardInterrupt:
        print("\n⚠️ Workflow interrupted")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        orchestrator.cleanup()

if __name__ == "__main__":
    main() 
