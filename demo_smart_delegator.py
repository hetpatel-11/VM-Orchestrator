import os
import time
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class DemoSmartDelegator:
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY', 'your_orgo_api_key_here')
        
        # For demo: using one working VM to show the concept
        print("🚀 Initializing Demo Smart Task Delegation System...")
        self.computer = Computer(project_id="yourcomputerid", api_key=self.api_key)
        print("✅ VM ready for intelligent task delegation!")
    
    def analyze_and_delegate_task(self, user_prompt):
        """Intelligently analyze user prompt and create appropriate task"""
        
        print(f"\n🧠 ANALYZING TASK: '{user_prompt}'")
        print("="*80)
        
        # Smart task analysis
        delegated_task = self.smart_task_analysis(user_prompt)
        
        print("🎯 INTELLIGENT TASK DELEGATION:")
        print(f"📝 Generated Task: {delegated_task[:150]}...")
        print("="*80)
        
        # Execute the intelligently generated task
        self.execute_smart_task(delegated_task)
    
    def smart_task_analysis(self, prompt):
        """Analyze prompt and create intelligent task delegation"""
        
        prompt_lower = prompt.lower()
        
        # RESEARCH & ANALYSIS PROMPTS
        if any(word in prompt_lower for word in ['research', 'analyze', 'study', 'investigate', 'find', 'search', 'explore', 'learn']):
            return f"""
            INTELLIGENT RESEARCH & ANALYSIS TASK for: "{prompt}"
            
            MULTI-STEP WORKFLOW:
            
            PHASE 1 - RESEARCH:
            1. Open browser and conduct comprehensive research on: {prompt}
            2. Search multiple authoritative sources (news, academic, industry reports)
            3. Gather current statistics, trends, and key data points
            4. Take detailed notes and organize findings
            
            PHASE 2 - ANALYSIS:
            5. Open spreadsheet application 
            6. Create data analysis with charts and visualizations
            7. Identify patterns, trends, and key insights
            8. Generate comparative analysis and metrics
            
            PHASE 3 - PRESENTATION:
            9. Open presentation software
            10. Create professional presentation with:
                - Executive summary of findings
                - Key data and visualizations
                - Insights and recommendations
                - Professional formatting and design
            
            11. Save all outputs: research_notes.txt, analysis.xlsx, presentation.pptx
            12. Take screenshots of key findings
            
            This simulates work that would normally be split across 3 VMs!
            """
        
        # BUSINESS & STRATEGY PROMPTS
        elif any(word in prompt_lower for word in ['business', 'company', 'market', 'strategy', 'plan', 'startup', 'competitive']):
            return f"""
            INTELLIGENT BUSINESS ANALYSIS TASK for: "{prompt}"
            
            COMPREHENSIVE BUSINESS WORKFLOW:
            
            MARKET RESEARCH PHASE:
            1. Research market conditions and industry landscape for: {prompt}
            2. Analyze competitors and market opportunities
            3. Gather financial data and industry benchmarks
            4. Study customer needs and market trends
            
            FINANCIAL ANALYSIS PHASE:
            5. Open spreadsheet and create financial models
            6. Build revenue projections and cost analysis
            7. Calculate ROI and investment scenarios
            8. Create business case with financial projections
            
            STRATEGY & PRESENTATION PHASE:
            9. Develop strategic recommendations
            10. Create executive business presentation with:
                - Market opportunity analysis
                - Competitive positioning
                - Financial projections and ROI
                - Strategic roadmap and action plan
                - Risk analysis and mitigation
            
            11. Generate final deliverables and executive summary
            
            Complete end-to-end business analysis workflow!
            """
        
        # CREATIVE & DEVELOPMENT PROMPTS
        elif any(word in prompt_lower for word in ['create', 'design', 'build', 'make', 'write', 'develop', 'content']):
            return f"""
            INTELLIGENT CREATIVE DEVELOPMENT TASK for: "{prompt}"
            
            CREATIVE WORKFLOW PROCESS:
            
            RESEARCH & INSPIRATION PHASE:
            1. Research best practices and examples for: {prompt}
            2. Gather inspiration, references, and benchmarks
            3. Study target audience and requirements
            4. Collect resources and creative assets
            
            DEVELOPMENT & PROCESSING PHASE:
            5. Process research into structured framework
            6. Create content outlines and development plan
            7. Build supporting materials and resources
            8. Organize and structure creative elements
            
            CREATION & PRESENTATION PHASE:
            9. Create the final deliverable for: {prompt}
            10. Design professional presentation showcasing:
                - Creative concept and approach
                - Development process and rationale
                - Final output with professional formatting
                - Implementation guidelines
                - Next steps and recommendations
            
            11. Generate multiple format outputs and documentation
            
            Complete creative development pipeline!
            """
        
        # DEFAULT COMPREHENSIVE ANALYSIS
        else:
            return f"""
            INTELLIGENT COMPREHENSIVE ANALYSIS TASK for: "{prompt}"
            
            COMPLETE ANALYSIS WORKFLOW:
            
            INFORMATION GATHERING:
            1. Conduct thorough research on: {prompt}
            2. Gather data from multiple reliable sources
            3. Collect current information, trends, and insights
            4. Document findings systematically
            
            DATA PROCESSING & ANALYSIS:
            5. Analyze and process all gathered information
            6. Create structured analysis with visualizations
            7. Identify key patterns, trends, and insights
            8. Generate actionable recommendations
            
            FINAL DELIVERABLE CREATION:
            9. Create comprehensive presentation including:
                - Executive summary and key findings
                - Detailed analysis with supporting data
                - Visual representations and charts
                - Conclusions and recommendations
                - Implementation roadmap
            
            10. Generate final polished deliverables
            11. Create summary report and documentation
            
            End-to-end comprehensive analysis workflow!
            """
    
    def execute_smart_task(self, task):
        """Execute the intelligently generated task"""
        
        print("\n🚀 EXECUTING INTELLIGENT TASK...")
        print("⚡ This simulates work across multiple VMs in one comprehensive workflow!")
        
        try:
            self.computer.prompt(task)
            print("\n✅ INTELLIGENT TASK DELEGATION COMPLETED!")
            print("🎉 Task successfully executed with smart workflow!")
        except Exception as e:
            print(f"\n❌ Error executing task: {e}")
    
    def cleanup(self):
        """Clean up VM connection"""
        try:
            self.computer.destroy()
            print("✅ VM cleaned up!")
        except Exception as e:
            print(f"⚠️ Cleanup warning: {e}")

def main():
    """Main interactive function"""
    delegator = DemoSmartDelegator()
    
    try:
        print("\n" + "="*80)
        print("🎯 DEMO: INTELLIGENT TASK DELEGATION SYSTEM")
        print("Enter ANY task and watch it get intelligently analyzed and executed!")
        print("(This demo simulates multi-VM workflow on one VM)")
        print("="*80)
        
        # Get user input
        user_prompt = input("\n💭 Enter your task/prompt: ").strip()
        
        if not user_prompt:
            print("❌ No prompt entered. Using demo task...")
            user_prompt = "Research the impact of artificial intelligence on healthcare"
        
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
