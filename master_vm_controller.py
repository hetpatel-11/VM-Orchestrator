import os
import time
import threading
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

class MasterVMController:
    def __init__(self):
        self.api_key = os.getenv('ORGO_API_KEY')
        
        # Initialize all 3 VMs simultaneously
        print("🚀 Initializing all VMs...")
        self.vm1 = Computer(project_id="yourcomputerid", api_key=self.api_key)  # Research & Analysis VM
        self.vm2 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Processing & Data VM  
        self.vm3 = Computer(project_id="yourcomputerid", api_key=self.api_key)   # Presentation & Output VM
        
        print("✅ All 3 VMs connected and ready!")
        
        # Status tracking
        self.vm1_status = "Ready"
        self.vm2_status = "Ready" 
        self.vm3_status = "Ready"
        
    def real_time_parallel_execution(self):
        """Execute interconnected tasks across all 3 VMs in real-time"""
        
        print("\n" + "="*80)
        print("🎯 STARTING REAL-TIME PARALLEL EXECUTION ACROSS ALL 3 VMs")
        print("="*80)
        
        # Create threads for all VMs to work simultaneously
        vm1_thread = threading.Thread(target=self.vm1_research_and_analysis)
        vm2_thread = threading.Thread(target=self.vm2_data_processing) 
        vm3_thread = threading.Thread(target=self.vm3_presentation_creation)
        
        # Start all VMs at the SAME TIME
        print("🚀 Launching all VMs simultaneously...")
        vm1_thread.start()
        vm2_thread.start() 
        vm3_thread.start()
        
        # Monitor progress in real-time
        self.monitor_progress(vm1_thread, vm2_thread, vm3_thread)
        
        # Wait for all to complete
        vm1_thread.join()
        vm2_thread.join()
        vm3_thread.join()
        
        print("\n" + "="*80)
        print("🎉 ALL VMs COMPLETED THEIR INTERCONNECTED TASKS!")
        print("="*80)
        
    def vm1_research_and_analysis(self):
        """VM1: Research and competitive analysis"""
        self.vm1_status = "Working"
        print("🔍 VM1: Starting research and analysis...")
        
        prompt = """
        RESEARCH & ANALYSIS MISSION:
        
        1. Open browser and research "AI automation tools 2024"
        2. Find top 5 companies in this space and analyze:
           - Their main products and features
           - Pricing models
           - Market positioning
           - Recent news and developments
        
        3. Open text editor and create detailed competitive analysis:
           - Company comparison table
           - Strengths and weaknesses
           - Market opportunities
           - Key insights for strategy
        
        4. Save research as 'competitive_analysis.txt'
        5. Take screenshot of your findings
        
        This research will feed into VM2's financial analysis and VM3's presentation.
        """
        
        try:
            self.vm1.prompt(prompt)
            self.vm1_status = "Completed"
            print("✅ VM1: Research and analysis COMPLETED!")
        except Exception as e:
            self.vm1_status = f"Error: {e}"
            print(f"❌ VM1 Error: {e}")
            
    def vm2_data_processing(self):
        """VM2: Data processing and financial modeling"""
        self.vm2_status = "Working"
        print("⚙️ VM2: Starting data processing and financial modeling...")
        
        prompt = """
        DATA PROCESSING & FINANCIAL MODELING MISSION:
        
        1. Open spreadsheet application (Numbers/Excel)
        2. Create comprehensive financial analysis for AI automation market:
           - Market size calculations ($50B+ market)
           - Revenue projections for next 3 years
           - Cost analysis for different business models
           - ROI calculations for automation investments
           
        3. Build interactive charts and graphs:
           - Market growth trends (line chart)
           - Company revenue comparison (bar chart) 
           - Cost breakdown analysis (pie chart)
           - Investment scenarios (scenario analysis)
           
        4. Create financial dashboard with key metrics
        5. Export as 'financial_analysis.xlsx'
        6. Take screenshot of your dashboard
        
        This financial data will be used in VM3's executive presentation.
        """
        
        try:
            self.vm2.prompt(prompt)
            self.vm2_status = "Completed"
            print("✅ VM2: Data processing and financial modeling COMPLETED!")
        except Exception as e:
            self.vm2_status = f"Error: {e}"
            print(f"❌ VM2 Error: {e}")
            
    def vm3_presentation_creation(self):
        """VM3: Presentation and final deliverable creation"""
        self.vm3_status = "Working"
        print("📊 VM3: Starting presentation creation...")
        
        prompt = """
        PRESENTATION & DELIVERABLE CREATION MISSION:
        
        1. Open presentation software (Keynote/PowerPoint)
        2. Create executive-level presentation on "AI Automation Market Analysis":
           
           SLIDE STRUCTURE:
           - Title: "AI Automation Market Analysis 2024"
           - Executive Summary (key findings)
           - Market Overview & Size
           - Competitive Landscape (top 5 players)
           - Financial Projections & ROI
           - Strategic Recommendations
           - Investment Opportunities
           - Next Steps & Timeline
           
        3. Use professional design with:
           - Consistent branding and colors
           - High-quality charts and visuals
           - Clean, executive-friendly layout
           
        4. Create separate summary document (1-page brief)
        5. Save presentation as 'AI_Automation_Analysis.pptx'
        6. Take screenshot of key slides
        
        This presentation combines research from VM1 and financial data from VM2.
        """
        
        try:
            self.vm3.prompt(prompt)
            self.vm3_status = "Completed"
            print("✅ VM3: Presentation creation COMPLETED!")
        except Exception as e:
            self.vm3_status = f"Error: {e}"
            print(f"❌ VM3 Error: {e}")
    
    def monitor_progress(self, vm1_thread, vm2_thread, vm3_thread):
        """Monitor all VMs in real-time"""
        print("\n📊 REAL-TIME VM MONITORING:")
        print("-" * 50)
        
        while vm1_thread.is_alive() or vm2_thread.is_alive() or vm3_thread.is_alive():
            print(f"🔍 VM1 Status: {self.vm1_status}")
            print(f"⚙️ VM2 Status: {self.vm2_status}")
            print(f"📊 VM3 Status: {self.vm3_status}")
            print("-" * 50)
            time.sleep(10)  # Update every 10 seconds
            
        # Final status
        print("\n🏁 FINAL STATUS:")
        print(f"🔍 VM1: {self.vm1_status}")
        print(f"⚙️ VM2: {self.vm2_status}")
        print(f"📊 VM3: {self.vm3_status}")
    
    def alternative_task_workflow(self):
        """Alternative workflow: E-commerce business analysis"""
        print("\n🛒 ALTERNATIVE WORKFLOW: E-COMMERCE BUSINESS ANALYSIS")
        
        # All VMs work on different aspects of e-commerce analysis
        vm1_thread = threading.Thread(target=self.vm1_ecommerce_research)
        vm2_thread = threading.Thread(target=self.vm2_ecommerce_analytics)
        vm3_thread = threading.Thread(target=self.vm3_ecommerce_strategy)
        
        vm1_thread.start()
        vm2_thread.start()
        vm3_thread.start()
        
        vm1_thread.join()
        vm2_thread.join() 
        vm3_thread.join()
        
    def vm1_ecommerce_research(self):
        """VM1: E-commerce market research"""
        prompt = """
        E-COMMERCE RESEARCH:
        1. Research top e-commerce trends for 2024
        2. Analyze Amazon, Shopify, and emerging platforms
        3. Study consumer behavior changes
        4. Create market research document
        """
        self.vm1.prompt(prompt)
        
    def vm2_ecommerce_analytics(self):
        """VM2: E-commerce data analytics"""
        prompt = """
        E-COMMERCE ANALYTICS:
        1. Create sales performance dashboards
        2. Build customer acquisition cost models
        3. Analyze conversion rate optimization
        4. Generate financial projections
        """
        self.vm2.prompt(prompt)
        
    def vm3_ecommerce_strategy(self):
        """VM3: E-commerce strategy presentation"""
        prompt = """
        E-COMMERCE STRATEGY:
        1. Create business strategy presentation
        2. Design marketing campaign materials
        3. Build investor pitch deck
        4. Create implementation roadmap
        """
        self.vm3.prompt(prompt)
    
    def cleanup(self):
        """Clean up all VM connections"""
        print("\n🧹 Cleaning up all VMs...")
        try:
            self.vm1.destroy()
            self.vm2.destroy()
            self.vm3.destroy()
            print("✅ All VMs cleaned up successfully!")
        except Exception as e:
            print(f"⚠️ Cleanup warning: {e}")

def main():
    """Main execution function"""
    controller = MasterVMController()
    
    try:
        # Run the main interconnected workflow
        controller.real_time_parallel_execution()
        
        # Uncomment to run alternative workflow:
        # controller.alternative_task_workflow()
        
    except KeyboardInterrupt:
        print("\n⚠️ Execution interrupted by user")
    except Exception as e:
        print(f"\n❌ Error in main execution: {e}")
    finally:
        controller.cleanup()

if __name__ == "__main__":
    print("🎯 MASTER VM CONTROLLER - REAL-TIME PARALLEL EXECUTION")
    print("=" * 80)
    main() 
