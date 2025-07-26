import os
import time
import threading
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class SmartTaskDelegator:
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY', 'your_orgo_api_key_here')
        
        # Initialize all 3 VMs
        print("🚀 Initializing Smart Task Delegation System...")
        self.vm1 = Computer(project_id="yourcomputerid", api_key=self.api_key)  # Research & Data Collection
        self.vm2 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Processing & Analysis  
        self.vm3 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Output & Presentation
        
        print("✅ All 3 VMs ready for intelligent task delegation!")
        
        # VM status tracking
        self.vm1_status = "Ready"
        self.vm2_status = "Ready" 
        self.vm3_status = "Ready"
    
    def analyze_and_delegate_task(self, user_prompt):
        """Intelligently break down user prompt and delegate across VMs"""
        
        print(f"\n🧠 ANALYZING TASK: '{user_prompt}'")
        print("="*80)
        
        # Smart task breakdown based on prompt analysis
        task_breakdown = self.smart_task_breakdown(user_prompt)
        
        print("🎯 TASK DELEGATION PLAN:")
        print(f"🔍 VM1 (Research): {task_breakdown['vm1_task'][:100]}...")
        print(f"⚙️ VM2 (Processing): {task_breakdown['vm2_task'][:100]}...")
        print(f"📊 VM3 (Output): {task_breakdown['vm3_task'][:100]}...")
        print("="*80)
        
        # Execute all VMs simultaneously
        self.execute_delegated_tasks(task_breakdown)
    
    def smart_task_breakdown(self, prompt):
        """AI-powered task breakdown logic"""
        
        # Analyze prompt for keywords and intent
        prompt_lower = prompt.lower()
        
        # Initialize task components
        vm1_task = ""  # Research & Data Collection
        vm2_task = ""  # Processing & Analysis
        vm3_task = ""  # Output & Presentation
        
        # RESEARCH-RELATED PROMPTS
        if any(word in prompt_lower for word in ['research', 'analyze', 'study', 'investigate', 'find', 'search', 'explore']):
            vm1_task = f"""
            RESEARCH MISSION for: "{prompt}"
            
            1. Open browser and conduct comprehensive research on the topic
            2. Gather data from multiple authoritative sources
            3. Collect relevant statistics, facts, and current information
            4. Take notes and organize findings systematically
            5. Save research data as 'research_data.txt'
            
            Focus on gathering raw information that VM2 can analyze and VM3 can present.
            """
            
            vm2_task = f"""
            ANALYSIS MISSION for: "{prompt}"
            
            1. Open spreadsheet application
            2. Process and analyze the research data
            3. Create data visualizations and trends analysis
            4. Generate insights and key findings
            5. Build comparative analysis and metrics
            6. Export analysis as 'data_analysis.xlsx'
            
            Transform raw research into actionable insights for presentation.
            """
            
            vm3_task = f"""
            PRESENTATION MISSION for: "{prompt}"
            
            1. Open presentation software
            2. Create professional presentation combining research and analysis
            3. Design clear, engaging slides with key findings
            4. Include executive summary and recommendations
            5. Add visual elements and professional formatting
            6. Save as 'final_presentation.pptx'
            
            Create compelling presentation of research findings and analysis.
            """
        
        # BUSINESS-RELATED PROMPTS
        elif any(word in prompt_lower for word in ['business', 'company', 'market', 'strategy', 'plan', 'startup']):
            vm1_task = f"""
            BUSINESS RESEARCH for: "{prompt}"
            
            1. Research market conditions and industry trends
            2. Study competitors and market opportunities
            3. Gather financial and market data
            4. Collect case studies and best practices
            5. Document findings for business analysis
            """
            
            vm2_task = f"""
            BUSINESS ANALYSIS for: "{prompt}"
            
            1. Create financial models and projections
            2. Analyze market data and competitive landscape
            3. Build business case with ROI calculations
            4. Generate strategic recommendations
            5. Create implementation timeline and budget
            """
            
            vm3_task = f"""
            BUSINESS PRESENTATION for: "{prompt}"
            
            1. Create executive business presentation
            2. Include market analysis and financial projections
            3. Add strategic recommendations and action plan
            4. Design professional business deck
            5. Create executive summary document
            """
        
        # CREATIVE/CONTENT PROMPTS
        elif any(word in prompt_lower for word in ['create', 'design', 'build', 'make', 'write', 'develop']):
            vm1_task = f"""
            CONTENT RESEARCH for: "{prompt}"
            
            1. Research best practices and examples
            2. Gather inspiration and reference materials
            3. Study target audience and requirements
            4. Collect relevant resources and assets
            5. Document research for creative development
            """
            
            vm2_task = f"""
            CONTENT DEVELOPMENT for: "{prompt}"
            
            1. Process research into structured content
            2. Organize materials and create outlines
            3. Develop content framework and structure
            4. Create supporting materials and resources
            5. Prepare content for final presentation
            """
            
            vm3_task = f"""
            CREATIVE OUTPUT for: "{prompt}"
            
            1. Create final creative deliverable
            2. Design professional presentation of work
            3. Add visual elements and polished formatting
            4. Create multiple format outputs
            5. Prepare final presentation package
            """
        
        # DEFAULT: GENERAL TASK BREAKDOWN
        else:
            vm1_task = f"""
            INFORMATION GATHERING for: "{prompt}"
            
            1. Research and gather relevant information about the topic
            2. Use browser to find authoritative sources
            3. Collect data, facts, and current information
            4. Organize findings systematically
            5. Prepare comprehensive information base
            """
            
            vm2_task = f"""
            DATA PROCESSING for: "{prompt}"
            
            1. Analyze and process gathered information
            2. Create structured analysis and insights
            3. Generate charts, graphs, or visual representations
            4. Identify patterns and key findings
            5. Prepare analysis for presentation
            """
            
            vm3_task = f"""
            OUTPUT CREATION for: "{prompt}"
            
            1. Create final deliverable presentation
            2. Combine research and analysis into cohesive output
            3. Design professional presentation format
            4. Include summary and recommendations
            5. Generate final polished deliverable
            """
        
        return {
            'vm1_task': vm1_task,
            'vm2_task': vm2_task, 
            'vm3_task': vm3_task
        }
    
    def execute_delegated_tasks(self, task_breakdown):
        """Execute tasks across all VMs simultaneously"""
        
        print("\n🚀 EXECUTING DELEGATED TASKS ACROSS ALL VMs...")
        
        # Create threads for parallel execution
        vm1_thread = threading.Thread(target=self.execute_vm1_task, args=(task_breakdown['vm1_task'],))
        vm2_thread = threading.Thread(target=self.execute_vm2_task, args=(task_breakdown['vm2_task'],))
        vm3_thread = threading.Thread(target=self.execute_vm3_task, args=(task_breakdown['vm3_task'],))
        
        # Start all VMs simultaneously
        vm1_thread.start()
        vm2_thread.start() 
        vm3_thread.start()
        
        # Monitor progress
        self.monitor_all_vms(vm1_thread, vm2_thread, vm3_thread)
        
        # Wait for completion
        vm1_thread.join()
        vm2_thread.join()
        vm3_thread.join()
        
        print("\n🎉 ALL VMs COMPLETED THEIR DELEGATED TASKS!")
    
    def execute_vm1_task(self, task):
        """Execute VM1 research task"""
        self.vm1_status = "Working"
        print("🔍 VM1: Starting research task...")
        try:
            self.vm1.prompt(task)
            self.vm1_status = "Completed"
            print("✅ VM1: Research COMPLETED!")
        except Exception as e:
            self.vm1_status = f"Error: {e}"
            print(f"❌ VM1 Error: {e}")
    
    def execute_vm2_task(self, task):
        """Execute VM2 processing task"""
        self.vm2_status = "Working"
        print("⚙️ VM2: Starting processing task...")
        try:
            self.vm2.prompt(task)
            self.vm2_status = "Completed"
            print("✅ VM2: Processing COMPLETED!")
        except Exception as e:
            self.vm2_status = f"Error: {e}"
            print(f"❌ VM2 Error: {e}")
    
    def execute_vm3_task(self, task):
        """Execute VM3 output task"""
        self.vm3_status = "Working"
        print("📊 VM3: Starting output task...")
        try:
            self.vm3.prompt(task)
            self.vm3_status = "Completed"
            print("✅ VM3: Output COMPLETED!")
        except Exception as e:
            self.vm3_status = f"Error: {e}"
            print(f"❌ VM3 Error: {e}")
    
    def monitor_all_vms(self, vm1_thread, vm2_thread, vm3_thread):
        """Real-time monitoring of all VMs"""
        print("\n📊 REAL-TIME VM MONITORING:")
        print("-" * 60)
        
        while vm1_thread.is_alive() or vm2_thread.is_alive() or vm3_thread.is_alive():
            print(f"🔍 VM1 (Research): {self.vm1_status}")
            print(f"⚙️ VM2 (Processing): {self.vm2_status}")
            print(f"📊 VM3 (Output): {self.vm3_status}")
            print("-" * 60)
            time.sleep(15)  # Update every 15 seconds
        
        # Final status report
        print("\n🏁 FINAL EXECUTION REPORT:")
        print(f"🔍 VM1 Research: {self.vm1_status}")
        print(f"⚙️ VM2 Processing: {self.vm2_status}")
        print(f"📊 VM3 Output: {self.vm3_status}")
    
    def cleanup(self):
        """Clean up all VM connections"""
        print("\n🧹 Cleaning up all VMs...")
        try:
            self.vm1.destroy()
            self.vm2.destroy()
            self.vm3.destroy()
            print("✅ All VMs cleaned up!")
        except Exception as e:
            print(f"⚠️ Cleanup warning: {e}")

def main():
    """Main interactive function"""
    delegator = SmartTaskDelegator()
    
    try:
        print("\n" + "="*80)
        print("🎯 SMART TASK DELEGATION SYSTEM")
        print("Enter ANY task and watch it get intelligently split across 3 VMs!")
        print("="*80)
        
        # Get user input
        user_prompt = input("\n💭 Enter your task/prompt: ").strip()
        
        if not user_prompt:
            print("❌ No prompt entered. Using demo task...")
            user_prompt = "Research and analyze the future of electric vehicles market"
        
        # Execute intelligent delegation
        delegator.analyze_and_delegate_task(user_prompt)
        
    except KeyboardInterrupt:
        print("\n⚠️ Execution interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        delegator.cleanup()

if __name__ == "__main__":
    main() 
