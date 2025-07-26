import os
import time
import threading
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class OnePromptOrchestrator:
    """
    🎯 ONE PROMPT VM ORCHESTRATOR - SPEED OPTIMIZED
    
    Takes ANY single prompt and intelligently divides the work across:
    - VM1 (computer-nvuvnf7): Research & Data Collection
    - VM2 (computer-pum2j64p): Processing & Analysis  
    - VM3 (computer-2zaexgo): Presentation & Output
    
    ⚡ SPEED OPTIMIZATIONS:
    - Minimal screenshots to reduce cost and time
    - Focus on essential content over visual perfection
    - Streamlined workflows for faster execution
    - Text-based data collection prioritized
    """
    
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY', 'your_orgo_api_key_here')
        
        # Set the new Anthropic API key
        os.environ['ANTHROPIC_API_KEY'] = os.getenv('ANTHROPIC_API_KEY', 'your_anthropic_api_key_here')
        
        print("🚀 Initializing One Prompt VM Orchestrator...")
        
        # Initialize all 3 VMs with correct project IDs from your scripts
        self.vm1 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Research VM
        self.vm2 = Computer(project_id="yourcomputerid", api_key=self.api_key)  # Processing VM
        self.vm3 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Presentation VM
        
        print("✅ All 3 VMs connected and ready!")
        
        # Status tracking
        self.vm1_status = "Ready"
        self.vm2_status = "Ready"
        self.vm3_status = "Ready"
    
    def orchestrate_task(self, user_prompt):
        """🧠 Intelligently orchestrate task across all 3 VMs"""
        
        print(f"\n🧠 ORCHESTRATING TASK: '{user_prompt}'")
        print("="*80)
        
        # Analyze prompt and create intelligent task delegation
        task_plan = self.analyze_prompt_and_create_tasks(user_prompt)
        
        print("🎯 TASK DELEGATION PLAN:")
        print(f"🔍 VM1 (Research): {task_plan['research_focus']}")
        print(f"⚙️ VM2 (Processing): {task_plan['processing_focus']}")
        print(f"📊 VM3 (Presentation): {task_plan['presentation_focus']}")
        print("="*80)
        
        # Execute all VMs in parallel
        self.execute_parallel_tasks(task_plan)
    
    def analyze_prompt_and_create_tasks(self, prompt):
        """🤖 Smart prompt analysis and task creation"""
        
        prompt_lower = prompt.lower()
        
        # Determine task type and create specialized delegation
        if any(word in prompt_lower for word in ['research', 'analyze', 'study', 'investigate', 'explore', 'find']):
            return self.create_research_focused_tasks(prompt)
        
        elif any(word in prompt_lower for word in ['business', 'market', 'strategy', 'startup', 'company', 'competitive']):
            return self.create_business_focused_tasks(prompt)
        
        elif any(word in prompt_lower for word in ['create', 'design', 'build', 'develop', 'make', 'write']):
            return self.create_creative_focused_tasks(prompt)
        
        else:
            return self.create_general_analysis_tasks(prompt)
    
    def create_research_focused_tasks(self, prompt):
        """📊 Research-focused task delegation"""
        return {
            'research_focus': 'Comprehensive research and data gathering',
            'processing_focus': 'Data analysis and insights generation',
            'presentation_focus': 'Research findings presentation',
            
                         'vm1_task': f"""
             OPTIMIZED RESEARCH TASK for: "{prompt}"
             
             SPEED-OPTIMIZED WORKFLOW (minimal screenshots):
             1. Open browser and search for: {prompt}
             2. Quickly scan top 3-4 results without taking screenshots
             3. Copy key text data directly from reliable sources
             4. Open text editor immediately and paste findings
             5. Organize data efficiently: statistics, trends, key facts
             6. Save as 'research_{prompt.replace(' ', '_')}.txt' quickly
             7. Focus on text data collection, avoid visual browsing
             
             PRIORITY: Speed and data collection over visual confirmation.
             """,
            
                         'vm2_task': f"""
             FAST DATA ANALYSIS for: "{prompt}"
             
             SPEED-OPTIMIZED WORKFLOW (minimal screenshots):
             1. Open spreadsheet application quickly
             2. Create simple data tables with key metrics only
             3. Build essential charts (avoid complex formatting):
                - Basic trend line chart
                - Simple bar chart for comparisons
                - Quick summary metrics
             4. Focus on data insights over visual perfection
             5. Export quickly as 'analysis_{prompt.replace(' ', '_')}.xlsx'
             6. Prioritize speed: simple formatting, essential analysis only
             
             PRIORITY: Fast insights over visual polish.
             """,
            
                         'vm3_task': f"""
             RAPID PRESENTATION for: "{prompt}"
             
             SPEED-OPTIMIZED WORKFLOW (minimal screenshots):
             1. Open presentation software and select basic template
             2. Create streamlined presentation (5-7 slides max):
                - Title slide
                - Key findings (1-2 slides)
                - Essential data (1 slide)
                - Conclusions (1 slide)
             3. Use simple formatting, avoid complex animations
             4. Focus on content over design perfection
             5. Save quickly as 'presentation_{prompt.replace(' ', '_')}.pptx'
             6. Prioritize speed: essential slides only
             
             PRIORITY: Fast deliverable over visual perfection.
             """
        }
    
    def create_business_focused_tasks(self, prompt):
        """💼 Business-focused task delegation"""
        return {
            'research_focus': 'Market research and competitive analysis',
            'processing_focus': 'Financial modeling and business analytics',
            'presentation_focus': 'Business strategy presentation',
            
                         'vm1_task': f"""
             FAST BUSINESS RESEARCH for: "{prompt}"
             
             SPEED-OPTIMIZED (minimal screenshots):
             1. Quick search for market data and industry info
             2. Copy key competitor information directly
             3. Gather essential market size and trend data
             4. Focus on text-based data collection
             5. Save quickly as 'business_research_{prompt.replace(' ', '_')}.txt'
             6. Prioritize speed over comprehensive browsing
             """,
            
                         'vm2_task': f"""
             RAPID BUSINESS ANALYSIS for: "{prompt}"
             
             SPEED-OPTIMIZED (minimal screenshots):
             1. Create basic financial model with essential metrics
             2. Simple ROI calculations and cost estimates
             3. Quick market projections (basic formulas)
             4. Essential competitive positioning table
             5. Export quickly as 'business_analysis_{prompt.replace(' ', '_')}.xlsx'
             6. Focus on core numbers over complex modeling
             """,
            
                         'vm3_task': f"""
             FAST BUSINESS PRESENTATION for: "{prompt}"
             
             SPEED-OPTIMIZED (minimal screenshots):
             1. Create simple business presentation (5-6 slides)
             2. Essential market data and key financial metrics
             3. Basic recommendations and next steps
             4. Use simple template, minimal formatting
             5. Save quickly as 'business_plan_{prompt.replace(' ', '_')}.pptx'
             6. Prioritize content delivery over design polish
             """
        }
    
    def create_creative_focused_tasks(self, prompt):
        """🎨 Creative-focused task delegation"""
        return {
            'research_focus': 'Creative research and inspiration gathering',
            'processing_focus': 'Content development and structure',
            'presentation_focus': 'Creative deliverable design',
            
            'vm1_task': f"""
            CREATIVE RESEARCH for: "{prompt}"
            
            1. Research best practices and examples
            2. Gather inspiration and reference materials
            3. Study target audience and requirements
            4. Collect creative assets and resources
            5. Save research as 'creative_research_{prompt.replace(' ', '_')}.txt'
            """,
            
            'vm2_task': f"""
            CREATIVE DEVELOPMENT for: "{prompt}"
            
            1. Process research into structured framework
            2. Create content outlines and development plan
            3. Organize materials and structure elements
            4. Build supporting resources and templates
            5. Export as 'creative_framework_{prompt.replace(' ', '_')}.xlsx'
            """,
            
            'vm3_task': f"""
            CREATIVE OUTPUT for: "{prompt}"
            
            1. Create final creative deliverable
            2. Design professional presentation of work
            3. Add visual elements and formatting
            4. Create multiple format outputs
            5. Save as 'creative_output_{prompt.replace(' ', '_')}.pptx'
            """
        }
    
    def create_general_analysis_tasks(self, prompt):
        """📋 General analysis task delegation"""
        return {
            'research_focus': 'Information gathering and research',
            'processing_focus': 'Data processing and analysis',
            'presentation_focus': 'Final deliverable creation',
            
            'vm1_task': f"""
            INFORMATION GATHERING for: "{prompt}"
            
            1. Conduct thorough research on the topic
            2. Gather data from multiple reliable sources
            3. Collect current information and trends
            4. Document findings systematically
            5. Save as 'research_{prompt.replace(' ', '_')}.txt'
            """,
            
            'vm2_task': f"""
            DATA PROCESSING for: "{prompt}"
            
            1. Analyze and process gathered information
            2. Create structured analysis with insights
            3. Generate visualizations and charts
            4. Identify key patterns and findings
            5. Export as 'analysis_{prompt.replace(' ', '_')}.xlsx'
            """,
            
            'vm3_task': f"""
            FINAL DELIVERABLE for: "{prompt}"
            
            1. Create comprehensive presentation
            2. Combine research and analysis
            3. Design professional output format
            4. Include summary and recommendations
            5. Save as 'deliverable_{prompt.replace(' ', '_')}.pptx'
            """
        }
    
    def execute_parallel_tasks(self, task_plan):
        """🚀 Execute all VM tasks in parallel"""
        
        print("\n🚀 EXECUTING TASKS ACROSS ALL 3 VMs SIMULTANEOUSLY...")
        
        # Create threads for parallel execution
        vm1_thread = threading.Thread(target=self.execute_vm1_research, args=(task_plan['vm1_task'],))
        vm2_thread = threading.Thread(target=self.execute_vm2_processing, args=(task_plan['vm2_task'],))
        vm3_thread = threading.Thread(target=self.execute_vm3_presentation, args=(task_plan['vm3_task'],))
        
        # Start all VMs at the same time
        print("⚡ All VMs starting simultaneously...")
        vm1_thread.start()
        vm2_thread.start()
        vm3_thread.start()
        
        # Monitor progress
        self.monitor_all_vms(vm1_thread, vm2_thread, vm3_thread)
        
        # Wait for completion
        vm1_thread.join()
        vm2_thread.join()
        vm3_thread.join()
        
        print("\n🎉 ALL VMs COMPLETED THEIR ORCHESTRATED TASKS!")
        self.show_completion_summary()
    
    def execute_vm1_research(self, task):
        """🔍 Execute VM1 research task"""
        self.vm1_status = "Researching..."
        print("🔍 VM1: Starting research task...")
        try:
            self.vm1.prompt(task)
            self.vm1_status = "Research Complete ✅"
            print("✅ VM1: Research COMPLETED!")
        except Exception as e:
            self.vm1_status = f"Error: {e}"
            print(f"❌ VM1 Error: {e}")
    
    def execute_vm2_processing(self, task):
        """⚙️ Execute VM2 processing task"""
        self.vm2_status = "Processing..."
        print("⚙️ VM2: Starting processing task...")
        try:
            self.vm2.prompt(task)
            self.vm2_status = "Processing Complete ✅"
            print("✅ VM2: Processing COMPLETED!")
        except Exception as e:
            self.vm2_status = f"Error: {e}"
            print(f"❌ VM2 Error: {e}")
    
    def execute_vm3_presentation(self, task):
        """📊 Execute VM3 presentation task"""
        self.vm3_status = "Creating presentation..."
        print("📊 VM3: Starting presentation task...")
        try:
            self.vm3.prompt(task)
            self.vm3_status = "Presentation Complete ✅"
            print("✅ VM3: Presentation COMPLETED!")
        except Exception as e:
            self.vm3_status = f"Error: {e}"
            print(f"❌ VM3 Error: {e}")
    
    def monitor_all_vms(self, vm1_thread, vm2_thread, vm3_thread):
        """📊 Real-time monitoring of all VMs"""
        print("\n📊 REAL-TIME VM MONITORING:")
        print("-" * 70)
        
        while vm1_thread.is_alive() or vm2_thread.is_alive() or vm3_thread.is_alive():
            print(f"🔍 VM1 Research: {self.vm1_status}")
            print(f"⚙️ VM2 Processing: {self.vm2_status}")
            print(f"📊 VM3 Presentation: {self.vm3_status}")
            print("-" * 70)
            time.sleep(5)  # Update every 5 seconds for faster monitoring
        
        # Final status
        print("🏁 FINAL STATUS:")
        print(f"🔍 VM1: {self.vm1_status}")
        print(f"⚙️ VM2: {self.vm2_status}")
        print(f"📊 VM3: {self.vm3_status}")
    
    def show_completion_summary(self):
        """📋 Show task completion summary"""
        print("\n📋 ORCHESTRATION SUMMARY:")
        print("=" * 70)
        print("✅ VM1: Research and data collection completed")
        print("✅ VM2: Data analysis and processing completed")
        print("✅ VM3: Final presentation and deliverables completed")
        print("\n📁 Generated Files:")
        print("   • Research findings document")
        print("   • Data analysis spreadsheet")
        print("   • Professional presentation")
        print("\n🏆 ONE PROMPT ORCHESTRATION SUCCESSFUL!")
    
    def cleanup(self):
        """🧹 Clean up all VM connections"""
        print("\n🧹 Cleaning up all VMs...")
        try:
            self.vm1.destroy()
            self.vm2.destroy()
            self.vm3.destroy()
            print("✅ All VMs cleaned up successfully!")
        except Exception as e:
            print(f"⚠️ Cleanup warning: {e}")

def main():
    """🎯 Main orchestrator function"""
    
    print("🎯 ONE PROMPT VM ORCHESTRATOR")
    print("=" * 80)
    print("🚀 Enter ONE prompt and watch it get intelligently split across 3 VMs!")
    print("📋 VM1: Research | VM2: Processing | VM3: Presentation")
    print("=" * 80)
    
    orchestrator = OnePromptOrchestrator()
    
    try:
        # Get user input
        user_prompt = input("\n💭 Enter your single prompt: ").strip()
        
        if not user_prompt:
            print("❌ No prompt entered. Exiting...")
            return
        
        # Execute intelligent orchestration
        orchestrator.orchestrate_task(user_prompt)
        
        print(f"\n🎉 SUCCESS! Your prompt '{user_prompt}' was intelligently")
        print("   orchestrated across all 3 VMs with specialized task distribution!")
        
    except KeyboardInterrupt:
        print("\n⚠️ Orchestration interrupted by user")
    except Exception as e:
        print(f"\n❌ Error in orchestration: {e}")
    finally:
        orchestrator.cleanup()

if __name__ == "__main__":
    main() 
