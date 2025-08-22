#!/usr/bin/env python3
"""
Lineage2M Master Enhancement Optimizer
Complete analysis system with tumbal destruction mechanics
Version: 2.0
"""

import json
import os
import sys
import time
import random
from datetime import datetime, timedelta
from collections import defaultdict, deque
import statistics
import math

# Import epic drop analyzer
from l2m_epic_drop_analyzer import L2MEpicDropAnalyzer

class L2MEnhancementMasterSystem:
    def __init__(self):
        self.version = "2.1"
        self.author = "L2M Community"
        self.last_update = datetime.now().isoformat()
        self.epic_analyzer = L2MEpicDropAnalyzer()
        
        # Actual game rates
        self.enhancement_rates = {
            'rare': {
                '+6_to_+7': 0.33,
                '+7_to_+8': 0.20,
                '+8_to_+9': 0.12,
                '+9_to_+10': 0.06
            },
            'unique': {
                '+6_to_+7': 0.30,
                '+7_to_+8': 0.18,
                '+8_to_+9': 0.10,
                '+9_to_+10': 0.05
            },
            'legendary': {
                '+6_to_+7': 0.28,
                '+7_to_+8': 0.16,
                '+8_to_+9': 0.08,
                '+9_to_+10': 0.04
            }
        }
        
        self.destruction_rates = {
            'rare': {
                '+6_to_+7': 0.20,
                '+7_to_+8': 0.30,
                '+8_to_+9': 0.40,
                '+9_to_+10': 0.50
            },
            'unique': {
                '+6_to_+7': 0.25,
                '+7_to_+8': 0.35,
                '+8_to_+9': 0.45,
                '+9_to_+10': 0.55
            }
        }
    
    def clear_screen(self):
        """Clear console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Print application header"""
        self.clear_screen()
        print("="*60)
        print("    LINEAGE2M ENHANCEMENT OPTIMIZER v2.0")
        print("    Tumbal Destruction Analysis System")
        print("="*60)
        print()
    
    def main_menu(self):
        """Display main menu"""
        print("\n📋 MAIN MENU:")
        print("="*40)
        print("Enhancement Tools:")
        print("1. Quick Enhancement Calculator")
        print("2. Tumbal Strategy Analysis") 
        print("3. Real-Time Enhancement Advisor")
        print("4. Success Rate Calculator")
        print("5. Economic Analysis (Diamond)")
        print("6. Tumbal Success Problem Solver")
        print()
        print("Epic Drop Tools:")
        print("7. Epic Drop Map Analysis")
        print("8. Field Boss Timers")
        print("9. Daily Farming Route")
        print()
        print("System:")
        print("10. Export Full Report")
        print("11. About & Help")
        print("12. Exit")
        print()
        return input("Select option (1-12): ")
    
    def quick_calculator(self):
        """Quick enhancement calculator"""
        self.print_header()
        print("🔮 QUICK ENHANCEMENT CALCULATOR\n")
        
        print("Select weapon grade:")
        print("1. Rare (Blue)")
        print("2. Unique (Purple)")
        print("3. Legendary (Orange)")
        grade_choice = input("\nChoice (1-3): ")
        
        grade_map = {'1': 'rare', '2': 'unique', '3': 'legendary'}
        grade = grade_map.get(grade_choice, 'rare')
        
        print("\nTarget enhancement level:")
        print("1. +6 → +7")
        print("2. +7 → +8")
        print("3. +8 → +9")
        print("4. +9 → +10")
        level_choice = input("\nChoice (1-4): ")
        
        level_map = {
            '1': '+6_to_+7',
            '2': '+7_to_+8',
            '3': '+8_to_+9',
            '4': '+9_to_+10'
        }
        level = level_map.get(level_choice, '+6_to_+7')
        
        tumbal_count = int(input("\nNumber of tumbal destroyed: "))
        
        # Calculate
        base_rate = self.enhancement_rates[grade][level]
        karma_boost = min(tumbal_count * 0.03, 0.30)
        final_rate = base_rate + karma_boost
        
        print("\n" + "="*50)
        print("📊 CALCULATION RESULTS:")
        print(f"• Weapon Grade: {grade.upper()}")
        print(f"• Enhancement: {level.replace('_to_', ' → ')}")
        print(f"• Base Rate: {base_rate*100:.1f}%")
        print(f"• Tumbal Destroyed: {tumbal_count}")
        print(f"• Karma Boost: +{karma_boost*100:.1f}%")
        print(f"• FINAL SUCCESS RATE: {final_rate*100:.1f}%")
        print(f"• Expected Attempts: {1/final_rate:.2f}")
        print("="*50)
        
        input("\nPress Enter to continue...")
    
    def tumbal_strategy_analysis(self):
        """Analyze tumbal strategy"""
        self.print_header()
        print("💀 TUMBAL STRATEGY ANALYSIS\n")
        
        strategies = {
            'RARE WEAPONS': {
                '+7 (33% base)': {
                    'tumbal_needed': '2-3 weapons',
                    'final_rate': '39-42%',
                    'recommendation': 'Optional, base rate decent'
                },
                '+8 (20% base)': {
                    'tumbal_needed': '5 weapons',
                    'final_rate': '35%',
                    'recommendation': 'Recommended, saves attempts'
                },
                '+9 (12% base)': {
                    'tumbal_needed': '8 weapons',
                    'final_rate': '36%',
                    'recommendation': 'MANDATORY - triples success'
                }
            },
            'UNIQUE WEAPONS': {
                '+7 (30% base)': {
                    'tumbal_needed': '3 weapons',
                    'final_rate': '39%',
                    'recommendation': 'Good value for expensive item'
                },
                '+8 (18% base)': {
                    'tumbal_needed': '6 weapons',
                    'final_rate': '36%',
                    'recommendation': 'Essential - doubles success'
                },
                '+9 (10% base)': {
                    'tumbal_needed': '10 weapons',
                    'final_rate': '40%',
                    'recommendation': 'MANDATORY - quadruples rate'
                }
            }
        }
        
        for grade, levels in strategies.items():
            print(f"\n[{grade}]")
            for level, data in levels.items():
                print(f"\n• {level}")
                print(f"  Tumbal: {data['tumbal_needed']}")
                print(f"  Success: {data['final_rate']}")
                print(f"  Note: {data['recommendation']}")
        
        print("\n" + "="*50)
        print("⚠️ TUMBAL SUCCESS PROBLEM:")
        print("• If tumbal succeeds +7 = karma reset!")
        print("• Solution: Use 8-10 tumbal (expect 2-3 success)")
        print("• Or use COMMON weapons (higher destroy rate)")
        print("="*50)
        
        input("\nPress Enter to continue...")
    
    def real_time_advisor(self):
        """Real-time enhancement advisor"""
        self.print_header()
        print("⏰ REAL-TIME ENHANCEMENT ADVISOR\n")
        
        current_time = datetime.now()
        hour = current_time.hour
        weekday = current_time.strftime('%A')
        
        # Time scoring
        time_scores = {
            range(0, 1): (95, '⭐⭐⭐⭐⭐', 'EXCELLENT - Daily reset!'),
            range(1, 6): (85, '⭐⭐⭐⭐', 'GOOD - Low population'),
            range(6, 10): (70, '⭐⭐⭐', 'ACCEPTABLE - Moderate'),
            range(10, 17): (50, '⭐⭐', 'POOR - Standard rates'),
            range(17, 20): (35, '⭐', 'BAD - High population'),
            range(20, 24): (25, '⭐', 'TERRIBLE - Peak hours')
        }
        
        score = 50
        rating = '⭐⭐'
        advice = 'Standard conditions'
        
        for time_range, (s, r, a) in time_scores.items():
            if hour in time_range:
                score, rating, advice = s, r, a
                break
        
        print(f"Current Time: {current_time.strftime('%Y-%m-%d %H:%M')}")
        print(f"Day: {weekday}")
        print(f"Hour: {hour:02d}:00")
        print()
        print(f"Timing Score: {score}/100 {rating}")
        print(f"Assessment: {advice}")
        print()
        
        if score >= 75:
            print("✅ RECOMMENDATION: ENHANCE NOW!")
            print("• Use your prepared tumbal")
            print("• Act quickly within 60 seconds")
        elif score >= 50:
            print("⚠️ RECOMMENDATION: PROCEED WITH CAUTION")
            print("• Use extra tumbal for safety")
            print("• Consider waiting for better time")
        else:
            print("❌ RECOMMENDATION: WAIT!")
            print(f"• Next good window: {(24-hour) if hour > 0 else 1} hours")
            print("• Save materials for better timing")
        
        print("\n" + "="*50)
        print("BEST ENHANCEMENT WINDOWS:")
        print("• 00:00-00:30: Daily reset (+20%)")
        print("• 02:00-06:00: Minimum load (+10%)")
        print("• Post-maintenance: 1-2 hours (+15%)")
        print("• Tuesday/Thursday: Best days")
        print("="*50)
        
        input("\nPress Enter to continue...")
    
    def success_rate_calculator(self):
        """Detailed success rate calculator"""
        self.print_header()
        print("📈 SUCCESS RATE CALCULATOR\n")
        
        print("Enter your scenario:")
        grade = input("Weapon grade (rare/unique/legendary): ").lower()
        current = int(input("Current level (+6, +7, +8, +9): "))
        target = current + 1
        tumbal = int(input("Tumbal destroyed: "))
        event = input("Event active? (y/n): ").lower() == 'y'
        
        level_key = f'+{current}_to_+{target}'
        
        try:
            base_rate = self.enhancement_rates.get(grade, self.enhancement_rates['rare']).get(level_key, 0.10)
        except:
            base_rate = 0.10
        
        karma_boost = min(tumbal * 0.03, 0.30)
        event_boost = 0.25 if event else 0
        
        final_rate = min(base_rate + karma_boost + event_boost, 0.75)
        
        attempts_needed = 1 / final_rate if final_rate > 0 else 999
        
        print("\n" + "="*50)
        print("📊 DETAILED CALCULATION:")
        print(f"• Base Rate: {base_rate*100:.1f}%")
        print(f"• Karma Boost: +{karma_boost*100:.1f}% ({tumbal} tumbal)")
        if event:
            print(f"• Event Boost: +{event_boost*100:.1f}%")
        print(f"• FINAL RATE: {final_rate*100:.1f}%")
        print()
        print(f"Expected Attempts: {attempts_needed:.2f}")
        print(f"90% Confidence: {attempts_needed*0.5:.1f}-{attempts_needed*2:.1f} attempts")
        
        # Diamond cost estimation
        diamond_per_attempt = 50 if current <= 7 else 100 if current == 8 else 200
        total_cost = attempts_needed * diamond_per_attempt
        
        print()
        print(f"💎 ESTIMATED COST:")
        print(f"• Per attempt: {diamond_per_attempt} diamonds")
        print(f"• Expected total: {total_cost:.0f} diamonds")
        print(f"• Worst case (2x): {total_cost*2:.0f} diamonds")
        print("="*50)
        
        input("\nPress Enter to continue...")
    
    def economic_analysis(self):
        """Economic analysis in diamonds"""
        self.print_header()
        print("💎 ECONOMIC ANALYSIS (DIAMOND CURRENCY)\n")
        
        print("CURRENT MARKET PRICES:")
        print("• Rare +6: 50-100 diamonds")
        print("• Rare +7: 300-500 diamonds")
        print("• Rare +8: 1500-2000 diamonds")
        print("• Rare +9: 5000+ diamonds")
        print()
        print("• Unique +6: 500-1000 diamonds")
        print("• Unique +7: 2000-3000 diamonds")
        print("• Unique +8: 8000-10000 diamonds")
        print("• Unique +9: 30000+ diamonds")
        
        print("\n" + "="*50)
        print("TUMBAL INVESTMENT ANALYSIS:")
        print()
        
        scenarios = [
            ("Rare +7", 5, 250, 400, "60% profit"),
            ("Rare +8", 8, 400, 1500, "275% profit"),
            ("Unique +7", 5, 250, 2500, "900% profit"),
            ("Unique +8", 10, 500, 8000, "1500% profit")
        ]
        
        for item, tumbal, cost, value, roi in scenarios:
            print(f"{item}:")
            print(f"  • Tumbal needed: {tumbal}")
            print(f"  • Investment: {cost} diamonds")
            print(f"  • Success value: {value} diamonds")
            print(f"  • ROI: {roi}")
            print()
        
        print("="*50)
        input("\nPress Enter to continue...")
    
    def tumbal_success_solver(self):
        """Solve tumbal success problem"""
        self.print_header()
        print("🎯 TUMBAL SUCCESS PROBLEM SOLVER\n")
        
        print("THE PROBLEM:")
        print("• You need 5 tumbal destroyed")
        print("• But tumbal #3 succeeds +7")
        print("• Karma reset to 0!")
        print()
        
        print("QUICK DECISION GUIDE:")
        print("="*50)
        print("If tumbal succeeds after:")
        print("• 0-1 destroyed → RESTART (need more)")
        print("• 2 destroyed → Borderline (50/50 decision)")
        print("• 3 destroyed → PROCEED (acceptable karma)")
        print("• 4+ destroyed → DEFINITELY PROCEED")
        print()
        
        print("SOLUTIONS:")
        print("="*50)
        print("1. USE COMMON WEAPONS")
        print("   • 40% destroy rate (vs 33% rare)")
        print("   • More likely to destroy")
        print()
        print("2. PREPARE MORE TUMBAL")
        print("   • Use 8-10 instead of 5")
        print("   • Expect 2-3 to succeed")
        print()
        print("3. HOT STREAK STRATEGY")
        print("   • 2+ tumbal success = HOT STREAK")
        print("   • Immediately attempt main weapon")
        print()
        print("4. PIVOT STRATEGY")
        print("   • Tumbal +7? Try +7→+8 on it")
        print("   • If destroys, karma continues")
        print("="*50)
        
        input("\nPress Enter to continue...")
    
    def export_report(self):
        """Export full analysis report"""
        self.print_header()
        print("📄 EXPORTING FULL REPORT...\n")
        
        report = {
            'generated': datetime.now().isoformat(),
            'version': self.version,
            'enhancement_rates': self.enhancement_rates,
            'destruction_rates': self.destruction_rates,
            'optimal_tumbal': {
                'rare': {
                    '+7': '2-3 tumbal',
                    '+8': '5 tumbal',
                    '+9': '8 tumbal'
                },
                'unique': {
                    '+7': '3 tumbal',
                    '+8': '6 tumbal',
                    '+9': '10 tumbal'
                }
            },
            'timing_windows': {
                'best': '00:00-00:30 daily reset',
                'good': '02:00-06:00 low population',
                'avoid': '19:00-23:00 peak hours'
            },
            'tumbal_problem_solutions': [
                'Use common weapons for higher destroy rate',
                'Prepare 8-10 tumbal instead of 5',
                'Exploit hot streaks when detected',
                'Make quick decisions based on destruction count'
            ]
        }
        
        filename = f"L2M_Enhancement_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
            print(f"✅ Report saved: {filename}")
        except Exception as e:
            print(f"❌ Error saving report: {e}")
        
        input("\nPress Enter to continue...")
    
    def epic_drop_map_analysis(self):
        """Analyze epic drop maps and rates"""
        self.print_header()
        print("🗺️ EPIC DROP MAP ANALYSIS\n")
        
        # Get current day analysis
        day_analysis = self.epic_analyzer.get_current_day_analysis()
        
        print(f"📅 Today: {day_analysis['current_day']}")
        print(f"Drop Rate Bonus: {day_analysis['bonus_percentage']}")
        print(f"Reason: {day_analysis['reason']}")
        print(f"Time Assessment: {day_analysis['time_bonus']}")
        print(f"Action: {day_analysis['recommended_action']}")
        
        if day_analysis['special_events'] != 'None':
            print(f"\n⚡ SPECIAL EVENT: {day_analysis['special_events']}")
        
        print("\n" + "="*50)
        print("BEST EPIC DROP MAPS BY LEVEL:")
        print("="*50)
        
        level_ranges = [
            (40, 50, "Level 40-50"),
            (50, 60, "Level 50-60"),
            (60, 70, "Level 60-70"),
            (70, 80, "Level 70+")
        ]
        
        for min_lvl, max_lvl, label in level_ranges:
            print(f"\n[{label}]")
            maps = self.epic_analyzer.epic_drop_maps.get(f'level_{min_lvl}_{max_lvl}', {})
            for map_name, map_data in list(maps.items())[:2]:
                print(f"\n• {map_name.replace('_', ' ')}")
                print(f"  Drop Rate: {map_data['drop_rate']}")
                print(f"  Best Time: {map_data['best_time']}")
                print(f"  Competition: {map_data['competition']}")
                print(f"  Items: {', '.join(map_data['epic_items'][:2])}")
        
        print("\n" + "="*50)
        print("💡 EPIC FARMING TIPS:")
        print("• Farm during 00:00-06:00 for low competition")
        print("• Wednesday/Weekend have drop rate bonuses")
        print("• Join world bosses for guaranteed epic chance")
        print("• Party farming gives +10% drop bonus")
        print("="*50)
        
        input("\nPress Enter to continue...")
    
    def field_boss_timers(self):
        """Show field boss spawn timers"""
        self.print_header()
        print("⏰ FIELD BOSS & WORLD BOSS TIMERS\n")
        
        # Get boss timers
        timers = self.epic_analyzer.get_boss_timers()
        
        print("UPCOMING WORLD BOSSES:")
        print("="*50)
        
        if timers:
            for timer in timers[:3]:  # Show next 3 bosses
                print(f"\n🔴 {timer['boss']}")
                print(f"   Spawn: {timer['spawn_time'].strftime('%A %H:%M')}")
                print(f"   Time Until: {timer['time_until']}")
                print(f"   Drops: {', '.join(timer['drops'])}")
        else:
            print("No scheduled world bosses in next 24 hours")
        
        print("\n" + "="*50)
        print("FIELD BOSS RESPAWN TIMES:")
        print("="*50)
        
        field_bosses = {
            'Contaminated Orc Chief': '2 hours',
            'Giant Wasteland Basilisk': '3 hours',
            'Death Knight': '4 hours',
            'Cursed Clara': '6 hours',
            'Core': '8-12 hours',
            'Orfen': '12-24 hours',
            'Queen Ant': '24-36 hours'
        }
        
        for boss, respawn in field_bosses.items():
            print(f"• {boss}: {respawn}")
        
        print("\n" + "="*50)
        print("WORLD BOSS SCHEDULE:")
        print("• Zaken: Wed & Sun 20:00")
        print("• Baium: Saturday 21:00")
        print("• Antharas: Special events only")
        print("• Valakas: Monthly events")
        print("="*50)
        
        input("\nPress Enter to continue...")
    
    def daily_farming_route(self):
        """Generate daily farming route recommendation"""
        self.print_header()
        print("🗺️ DAILY FARMING ROUTE RECOMMENDATION\n")
        
        print("Enter your character level: ", end='')
        try:
            level = int(input())
        except:
            level = 60
        
        routes = self.epic_analyzer.get_recommended_farming_route(level)
        
        print(f"\n📊 Recommended Route for Level {level}:")
        print("="*50)
        
        if routes:
            for route in routes:
                print(f"\nPriority {route['priority']}: {route['map']}")
                print(f"  Reason: {route['reason']}")
                print(f"  Epic Rate: {route['epic_rate']}")
                print(f"  Target Items: {', '.join(route['items'])}")
        else:
            print("No specific route for this level")
        
        # Daily optimization
        current_hour = datetime.now().hour
        print("\n" + "="*50)
        print("TODAY'S OPTIMIZATION:")
        print("="*50)
        
        if 0 <= current_hour < 6:
            print("✅ PRIME TIME NOW! (00:00-06:00)")
            print("• Lowest competition")
            print("• Best drop rates")
            print("• Farm elite zones")
        elif 6 <= current_hour < 12:
            print("⚠️ MODERATE TIME (06:00-12:00)")
            print("• Medium competition")
            print("• Focus on less popular maps")
        elif 12 <= current_hour < 19:
            print("❌ POOR TIME (12:00-19:00)")
            print("• High competition")
            print("• Consider waiting or do quests")
        else:
            print("⚡ BOSS TIME (19:00-24:00)")
            print("• Check for world bosses")
            print("• Join raid parties")
        
        # Special day bonuses
        day_analysis = self.epic_analyzer.get_current_day_analysis()
        if day_analysis['bonus_percentage'] != "+0%":
            print(f"\n🎁 TODAY'S BONUS: {day_analysis['bonus_percentage']}")
            print(f"Recommended maps: {', '.join(day_analysis['recommended_maps'][:2])}")
        
        print("="*50)
        input("\nPress Enter to continue...")
    
    def about_help(self):
        """Display about and help information"""
        self.print_header()
        print("ℹ️ ABOUT & HELP\n")
        
        print("LINEAGE2M ENHANCEMENT OPTIMIZER v2.0")
        print("="*50)
        print()
        print("This tool helps you optimize enhancement success")
        print("using the tumbal (sacrificial item) system.")
        print()
        print("KEY CONCEPTS:")
        print("• Tumbal: Items destroyed to build karma")
        print("• Karma: Hidden counter that boosts success")
        print("• Each destruction adds ~3% success rate")
        print("• Maximum karma boost: 30%")
        print()
        print("CRITICAL TIMING:")
        print("• 0-60 seconds after tumbal: 100% karma")
        print("• 60-120 seconds: 90% karma")
        print("• 2-5 minutes: 70% karma")
        print("• 5+ minutes: Karma expired!")
        print()
        print("REMEMBER:")
        print("• More tumbal = higher success")
        print("• Timing is critical")
        print("• Stop after failures")
        print("• Track your patterns")
        print()
        print("="*50)
        print("Created for L2M community")
        print("Use at your own risk!")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main application loop"""
        while True:
            self.print_header()
            choice = self.main_menu()
            
            if choice == '1':
                self.quick_calculator()
            elif choice == '2':
                self.tumbal_strategy_analysis()
            elif choice == '3':
                self.real_time_advisor()
            elif choice == '4':
                self.success_rate_calculator()
            elif choice == '5':
                self.economic_analysis()
            elif choice == '6':
                self.tumbal_success_solver()
            elif choice == '7':
                self.epic_drop_map_analysis()
            elif choice == '8':
                self.field_boss_timers()
            elif choice == '9':
                self.daily_farming_route()
            elif choice == '10':
                self.export_report()
            elif choice == '11':
                self.about_help()
            elif choice == '12':
                print("\nThank you for using L2M Enhancement Optimizer!")
                print("Good luck with your enhancements and epic farming!")
                time.sleep(2)
                break
            else:
                print("\nInvalid choice. Please try again.")
                time.sleep(1)

def main():
    """Entry point"""
    app = L2MEnhancementMasterSystem()
    app.run()

if __name__ == "__main__":
    main()