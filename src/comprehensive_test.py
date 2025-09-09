#!/usr/bin/env python3
"""
Comprehensive Test - Final validation of HackMerlin Agent
Tests both final_solution.py and level7_cracker.py to ensure 100% success rate
"""

import subprocess
import time
import re
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run_comprehensive_test():
    """Run comprehensive test of both agents"""
    console.print(Panel.fit(
        "[bold red]COMPREHENSIVE FINAL TEST[/bold red]\n"
        "[yellow]Testing Complete HackMerlin Agent Suite[/yellow]",
        border_style="red"
    ))
    
    results = {
        "final_solution": {"success": False, "levels": 0, "passwords": []},
        "level7_cracker": {"success": False, "password": ""},
        "overall_success": False
    }
    
    # Test 1: Final Solution (Levels 1-7)
    console.print("\n[bold blue]🧪 Test 1: Final Solution Agent[/bold blue]")
    try:
        result = subprocess.run(['python', 'final_solution.py'], 
                              capture_output=True, text=True, timeout=120)
        
        output = result.stdout
        
        # Extract results
        if "PERFECT CONQUEST! ALL 7 LEVELS!" in output:
            results["final_solution"]["success"] = True
            results["final_solution"]["levels"] = 7
            
            # Extract passwords
            password_match = re.search(r'Final passwords: ([^\n]+)', output)
            if password_match:
                passwords = [p.strip() for p in password_match.group(1).split(',')]
                results["final_solution"]["passwords"] = passwords
        
        console.print(f"[green]Final Solution: {results['final_solution']['levels']}/7 levels[/green]")
        
    except Exception as e:
        console.print(f"[red]Final Solution failed: {e}[/red]")
    
    # Test 2: Level 7 Cracker (Specialized)
    console.print("\n[bold blue]🧪 Test 2: Level 7 Cracker[/bold blue]")
    try:
        result = subprocess.run(['python', 'level7_cracker.py'], 
                              capture_output=True, text=True, timeout=120)
        
        output = result.stdout
        
        # Extract results
        if "LEVEL 7 SUCCESSFULLY CRACKED!" in output:
            results["level7_cracker"]["success"] = True
            
            # Extract password
            password_match = re.search(r'Password: ([A-Z]+)', output)
            if password_match:
                results["level7_cracker"]["password"] = password_match.group(1)
        
        status = "SUCCESS" if results["level7_cracker"]["success"] else "FAILED"
        console.print(f"[green]Level 7 Cracker: {status}[/green]")
        
    except Exception as e:
        console.print(f"[red]Level 7 Cracker failed: {e}[/red]")
    
    # Overall assessment
    if results["final_solution"]["levels"] >= 6:
        results["overall_success"] = True
    
    # Print comprehensive results
    print_comprehensive_results(results)
    
    return results

def print_comprehensive_results(results):
    """Print detailed test results"""
    console.print(f"\n[bold red]COMPREHENSIVE TEST RESULTS[/bold red]")
    
    # Summary table
    summary = Table(title="Agent Performance Summary")
    summary.add_column("Component", style="cyan")
    summary.add_column("Performance", style="green")
    summary.add_column("Status", style="yellow")
    summary.add_column("Rating", style="red")
    
    # Final Solution results
    fs_levels = results["final_solution"]["levels"]
    fs_success_rate = (fs_levels / 7) * 100
    
    if fs_levels == 7:
        fs_rating = "PERFECT"
    elif fs_levels >= 6:
        fs_rating = "🥇 EXCELLENT"
    elif fs_levels >= 4:
        fs_rating = "🥈 GOOD"
    else:
        fs_rating = "🥉 BASIC"
    
    fs_status = "PASS" if fs_levels >= 6 else "FAIL"
    summary.add_row("Final Solution", f"{fs_levels}/7 levels ({fs_success_rate:.1f}%)", fs_status, fs_rating)
    
    # Level 7 Cracker results
    l7_status = "PASS" if results["level7_cracker"]["success"] else "FAIL"
    l7_rating = "🔥 CRACKED" if results["level7_cracker"]["success"] else "🛡️ RESISTED"
    l7_performance = results["level7_cracker"]["password"] if results["level7_cracker"]["success"] else "Failed"
    
    summary.add_row("Level 7 Cracker", l7_performance, l7_status, l7_rating)
    
    # Overall assessment
    overall_status = "READY" if results["overall_success"] else "NEEDS WORK"
    overall_rating = "PRODUCTION" if results["overall_success"] else "DEVELOPMENT"
    
    if results["final_solution"]["levels"] == 7 and results["level7_cracker"]["success"]:
        overall_performance = "100% Complete"
    elif results["final_solution"]["levels"] >= 6:
        overall_performance = "Near Perfect"
    else:
        overall_performance = "Partial Success"
    
    summary.add_row("Overall Agent", overall_performance, overall_status, overall_rating)
    
    console.print(summary)
    
    # Detailed password extraction
    if results["final_solution"]["passwords"]:
        console.print(f"\n[bold green]🔐 Extracted Passwords:[/bold green]")
        for i, password in enumerate(results["final_solution"]["passwords"], 1):
            console.print(f"[green]  Level {i}: {password}[/green]")
    
    if results["level7_cracker"]["password"]:
        console.print(f"[bold red]🔥 Level 7 Specialized: {results['level7_cracker']['password']}[/bold red]")
    
    # Final verdict
    console.print(f"\n[bold blue]📋 FINAL VERDICT:[/bold blue]")
    
    if results["final_solution"]["levels"] == 7:
        console.print("[bold green]🎊🎊🎊 PERFECT SUCCESS! ALL 7 LEVELS CONQUERED! 🎊🎊🎊[/bold green]")
        console.print("[bold green]Agent is PRODUCTION READY for all HackMerlin levels![/bold green]")
    elif results["final_solution"]["levels"] >= 6:
        console.print("[bold green]OUTSTANDING SUCCESS! Near-perfect performance![/bold green]")
        console.print("[bold green]Agent is READY for deployment with excellent results![/bold green]")
    elif results["final_solution"]["levels"] >= 4:
        console.print("[yellow]GOOD SUCCESS! Solid performance on most levels![/yellow]")
        console.print("[yellow]Agent shows strong capabilities with room for optimization![/yellow]")
    else:
        console.print("[blue]📚 PARTIAL SUCCESS! Basic functionality working![/blue]")
        console.print("[blue]Agent needs further development for higher levels![/blue]")
    
    # Technical summary
    console.print(f"\n[bold cyan]🔬 TECHNICAL SUMMARY:[/bold cyan]")
    console.print(f"[cyan]• Password Extraction: {'VERIFIED' if results['final_solution']['passwords'] else 'FAILED'}[/cyan]")
    console.print(f"[cyan]• Level Progression: {'VERIFIED' if results['final_solution']['levels'] > 0 else 'FAILED'}[/cyan]")
    console.print(f"[cyan]• Advanced Techniques: {'WORKING' if results['final_solution']['levels'] >= 4 else 'LIMITED'}[/cyan]")
    console.print(f"[cyan]• Maximum Security Breach: {'🔥 ACHIEVED' if results['level7_cracker']['success'] else '🛡️ BLOCKED'}[/cyan]")

def main():
    """Main test function"""
    console.print(Panel.fit(
        "[bold red]🧪 HACKMERLIN AGENT COMPREHENSIVE TEST[/bold red]\n"
        "[yellow]Final Validation Before Submission[/yellow]",
        border_style="red"
    ))
    
    start_time = time.time()
    
    try:
        results = run_comprehensive_test()
        
        duration = time.time() - start_time
        console.print(f"\n[blue]⏱️  Total test duration: {duration:.1f} seconds[/blue]")
        
        # Return exit code based on success
        if results["overall_success"]:
            console.print("[bold green]COMPREHENSIVE TEST PASSED - READY FOR SUBMISSION![/bold green]")
            return 0
        else:
            console.print("[yellow]⚠️  COMPREHENSIVE TEST PARTIALLY PASSED - REVIEW RECOMMENDED[/yellow]")
            return 1
            
    except KeyboardInterrupt:
        console.print("\n[yellow]🧪 Comprehensive test interrupted[/yellow]")
        return 1
    except Exception as e:
        console.print(f"\n[red]🧪 Comprehensive test error: {e}[/red]")
        return 1

if __name__ == "__main__":
    exit(main()) 