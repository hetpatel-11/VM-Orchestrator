import os
import time
import threading
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class UltraOptimizedOrchestrator:
    """
    🚀 ULTRA-OPTIMIZED VM ORCHESTRATOR - MAXIMUM SPEED
    
    SMART TIME-SAVING TECHNIQUES:
    - Staggered VM starts (VM1 starts first, others follow data flow)
    - Pre-built templates and shortcuts
    - Conditional execution (skip steps if data exists)
    - Keyboard shortcuts over mouse clicks
    - Parallel prep work
    """
    
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY', 'your_orgo_api_key_here')
        
        # Set the new Anthropic API key
        os.environ['ANTHROPIC_API_KEY'] = os.getenv('ANTHROPIC_API_KEY', 'your_anthropic_api_key_here')
        
        print("🚀 Initializing ULTRA-OPTIMIZED Orchestrator...")
        
        # Initialize VMs but don't start tasks yet
        self.vm1 = Computer(project_id="computer-ykl00rx", api_key=self.api_key)   
        self.vm2 = Computer(project_id="computer-aspt7cz", api_key=self.api_key)  
        self.vm3 = Computer(project_id="computer-62gnt6i", api_key=self.api_key)   
        
        print("✅ All VMs ready for ULTRA-FAST execution!")
        
        self.vm1_status = "Ready"
        self.vm2_status = "Ready"
        self.vm3_status = "Ready"
    
    def smart_orchestrate(self, user_prompt):
        """🧠 SMART ORCHESTRATION with time-saving optimizations"""
        
        print(f"\n🧠 ULTRA-FAST ORCHESTRATION: '{user_prompt}'")
        print("="*80)
        
        # Quick prompt analysis
        task_plan = self.rapid_task_analysis(user_prompt)
        
        print("⚡ SMART EXECUTION PLAN:")
        print(f"🔍 VM1: {task_plan['vm1_focus']}")
        print(f"⚙️ VM2: {task_plan['vm2_focus']}")
        print(f"📊 VM3: {task_plan['vm3_focus']}")
        print("="*80)
        
        # SMART EXECUTION: Staggered start for data flow efficiency
        self.smart_staggered_execution(task_plan)
    
    def rapid_task_analysis(self, prompt):
        """⚡ ULTRA-FAST prompt analysis"""
        prompt_lower = prompt.lower()
        
        # Smart keyword detection
        if any(word in prompt_lower for word in ['research', 'analyze', 'study']):
            return self.create_speed_research_tasks(prompt)
        elif any(word in prompt_lower for word in ['business', 'market', 'startup']):
            return self.create_speed_business_tasks(prompt)
        else:
            return self.create_speed_general_tasks(prompt)
    
    def create_speed_research_tasks(self, prompt):
        """🔍 SPEED-OPTIMIZED research tasks"""
        return {
            'vm1_focus': 'Lightning-fast research collection',
            'vm2_focus': 'Instant data processing',
            'vm3_focus': 'Rapid presentation creation',
            
            'vm1_task': f"""
            LIGHTNING RESEARCH for: "{prompt}"
            
            ULTRA-SPEED WORKFLOW:
            1. Use Cmd+T for new tab (keyboard shortcut)
            2. Type search query and hit Enter immediately
            3. Cmd+C to copy key data from first 2 results ONLY
            4. Cmd+Tab to switch to text editor instantly
            5. Cmd+V to paste, add quick bullet points
            6. Cmd+S to save as 'research_{prompt.replace(' ', '_')}.txt'
            
            TIME TARGET: Complete in 2-3 minutes maximum
            NO SCREENSHOTS, NO BROWSING, COPY-PASTE ONLY
            """,
            
            'vm2_task': f"""
            INSTANT ANALYSIS for: "{prompt}"
            
            ULTRA-SPEED WORKFLOW:
            1. Cmd+Space to open Spotlight, type "Numbers" + Enter
            2. Use pre-built template (avoid starting from scratch)
            3. Create 3 columns only: Data, Value, Trend
            4. Add basic chart (Cmd+Option+C for quick chart)
            5. Cmd+S to save as 'analysis_{prompt.replace(' ', '_')}.xlsx'
            
            TIME TARGET: Complete in 3-4 minutes maximum
            BASIC CHARTS ONLY, NO COMPLEX FORMATTING
            """,
            
            'vm3_task': f"""
            RAPID PRESENTATION for: "{prompt}"
            
            ULTRA-SPEED WORKFLOW:
            1. Cmd+Space, type "Keynote" + Enter
            2. Select basic template (first option)
            3. Create 4 slides ONLY:
               - Title (30 seconds)
               - Key Findings (1 minute)
               - Data Summary (1 minute)  
               - Conclusion (30 seconds)
            4. Cmd+S to save as 'presentation_{prompt.replace(' ', '_')}.pptx'
            
            TIME TARGET: Complete in 3 minutes maximum
            NO ANIMATIONS, BASIC TEXT ONLY
            """
        }
    
    def create_speed_business_tasks(self, prompt):
        """💼 SPEED-OPTIMIZED business tasks"""
        return {
            'vm1_focus': 'Quick market research',
            'vm2_focus': 'Fast financial basics',
            'vm3_focus': 'Simple business deck',
            
            'vm1_task': f"""
            QUICK BUSINESS RESEARCH for: "{prompt}"
            
            SPEED WORKFLOW:
            1. Search for "{prompt} market size" immediately
            2. Copy first statistic found (Cmd+C)
            3. Search "competitors {prompt}" 
            4. Copy top 3 company names
            5. Open TextEdit, paste all data
            6. Save quickly as 'biz_research_{prompt.replace(' ', '_')}.txt'
            
            TIME TARGET: 2 minutes maximum
            """,
            
            'vm2_task': f"""
            BASIC FINANCIAL MODEL for: "{prompt}"
            
            SPEED WORKFLOW:
            1. Open Numbers with basic template
            2. Create simple 3-year projection table
            3. Add basic revenue/cost rows only
            4. One simple bar chart
            5. Save as 'biz_model_{prompt.replace(' ', '_')}.xlsx'
            
            TIME TARGET: 3 minutes maximum
            """,
            
            'vm3_task': f"""
            SIMPLE BUSINESS DECK for: "{prompt}"
            
            SPEED WORKFLOW:
            1. Keynote basic template
            2. 5 slides only: Title, Problem, Solution, Market, Plan
            3. Bullet points only, no graphics
            4. Save as 'biz_deck_{prompt.replace(' ', '_')}.pptx'
            
            TIME TARGET: 3 minutes maximum
            """
        }
    
    def create_speed_general_tasks(self, prompt):
        """📋 SPEED-OPTIMIZED general tasks"""
        return {
            'vm1_focus': 'Fast info gathering',
            'vm2_focus': 'Quick processing',
            'vm3_focus': 'Basic deliverable',
            
            'vm1_task': f"""
            FAST INFO GATHERING for: "{prompt}"
            
            1. Quick Google search
            2. Copy key facts from top 2 results
            3. Save in text file immediately
            
            TIME TARGET: 2 minutes
            """,
            
            'vm2_task': f"""
            QUICK PROCESSING for: "{prompt}"
            
            1. Basic spreadsheet with key data
            2. Simple summary table
            3. Save quickly
            
            TIME TARGET: 2 minutes
            """,
            
            'vm3_task': f"""
            BASIC DELIVERABLE for: "{prompt}"
            
            1. Simple 3-slide presentation
            2. Essential info only
            3. Save and done
            
            TIME TARGET: 2 minutes
            """
        }
    
    def smart_staggered_execution(self, task_plan):
        """🚀 SMART STAGGERED EXECUTION for maximum efficiency"""
        
        print("\n🚀 SMART STAGGERED EXECUTION:")
        print("⚡ VM1 starts immediately (data collection)")
        print("⏱️ VM2 starts after 1 minute (has some data to work with)")  
        print("⏱️ VM3 starts after 2 minutes (has data from both VMs)")
        print("="*80)
        
        # Start VM1 immediately
        vm1_thread = threading.Thread(target=self.execute_vm1_ultra_fast, args=(task_plan['vm1_task'],))
        vm1_thread.start()
        
        # Start VM2 after short delay (can use some data from VM1)
        time.sleep(60)  # 1 minute delay
        vm2_thread = threading.Thread(target=self.execute_vm2_ultra_fast, args=(task_plan['vm2_task'],))
        vm2_thread.start()
        
        # Start VM3 after another delay (can use data from VM1 and VM2)
        time.sleep(60)  # Another 1 minute delay
        vm3_thread = threading.Thread(target=self.execute_vm3_ultra_fast, args=(task_plan['vm3_task'],))
        vm3_thread.start()
        
        # Monitor with faster updates
        self.ultra_fast_monitoring(vm1_thread, vm2_thread, vm3_thread)
        
        # Wait for all completion
        vm1_thread.join()
        vm2_thread.join()
        vm3_thread.join()
        
        print("\n🎉 ULTRA-FAST ORCHESTRATION COMPLETE!")
        self.show_speed_summary()
    
    def execute_vm1_ultra_fast(self, task):
        """🔍 ULTRA-FAST VM1 execution"""
        self.vm1_status = "Speed Research..."
        try:
            self.vm1.prompt(task)
            self.vm1_status = "Research Complete ⚡"
        except Exception as e:
            self.vm1_status = f"Error: {e}"
    
    def execute_vm2_ultra_fast(self, task):
        """⚙️ ULTRA-FAST VM2 execution"""
        self.vm2_status = "Speed Processing..."
        try:
            self.vm2.prompt(task)
            self.vm2_status = "Processing Complete ⚡"
        except Exception as e:
            self.vm2_status = f"Error: {e}"
    
    def execute_vm3_ultra_fast(self, task):
        """📊 ULTRA-FAST VM3 execution"""
        self.vm3_status = "Speed Presentation..."
        try:
            self.vm3.prompt(task)
            self.vm3_status = "Presentation Complete ⚡"
        except Exception as e:
            self.vm3_status = f"Error: {e}"
    
    def ultra_fast_monitoring(self, vm1_thread, vm2_thread, vm3_thread):
        """📊 ULTRA-FAST monitoring"""
        while vm1_thread.is_alive() or vm2_thread.is_alive() or vm3_thread.is_alive():
            print(f"🔍 VM1: {self.vm1_status} | ⚙️ VM2: {self.vm2_status} | 📊 VM3: {self.vm3_status}")
            time.sleep(3)  # Even faster updates
    
    def show_speed_summary(self):
        """⚡ Show speed optimization summary"""
        print("\n⚡ ULTRA-OPTIMIZATION SUMMARY:")
        print("=" * 70)
        print("🚀 SPEED TECHNIQUES USED:")
        print("  • Staggered execution (data flow optimization)")
        print("  • Keyboard shortcuts (faster than mouse)")
        print("  • Pre-built templates (no setup time)")
        print("  • Minimal content targets (2-4 minutes per VM)")
        print("  • No screenshots policy")
        print("  • Copy-paste workflows")
        print("\n📁 DELIVERABLES CREATED IN RECORD TIME!")
    
    def cleanup(self):
        """🧹 Quick cleanup"""
        try:
            self.vm1.destroy()
            self.vm2.destroy()
            self.vm3.destroy()
        except Exception as e:
            print(f"⚠️ {e}")

def main():
    """⚡ ULTRA-FAST main execution"""
    print("⚡ ULTRA-OPTIMIZED VM ORCHESTRATOR")
    print("🚀 MAXIMUM SPEED & EFFICIENCY")
    print("=" * 80)
    
    orchestrator = UltraOptimizedOrchestrator()
    
    try:
        user_prompt = input("\n💭 Enter prompt for ULTRA-FAST execution: ").strip()
        
        if not user_prompt:
            print("❌ No prompt entered.")
            return
        
        start_time = time.time()
        orchestrator.smart_orchestrate(user_prompt)
        end_time = time.time()
        
        print(f"\n⚡ TOTAL EXECUTION TIME: {end_time - start_time:.2f} seconds")
        print("🏆 ULTRA-OPTIMIZATION SUCCESSFUL!")
        
    except KeyboardInterrupt:
        print("\n⚠️ Interrupted")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        orchestrator.cleanup()

if __name__ == "__main__":
    main() 