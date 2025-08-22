#!/usr/bin/env python3
"""
Lineage2M Epic Drop Map Analyzer
Field Boss & World Boss Timer System
"""

import json
from datetime import datetime, timedelta
import time

class L2MEpicDropAnalyzer:
    def __init__(self):
        # Field Boss spawn schedules (server time UTC+9 Korea)
        self.field_bosses = {
            'regular_field_bosses': {
                'Contaminated_Orc_Chief': {
                    'level': 45,
                    'respawn_time': '2 hours',
                    'location': 'Orc Barracks',
                    'drops': {
                        'epic_chance': '0.5-1%',
                        'items': ['Orc Chief Ring', 'Warrior Belt'],
                        'best_time': 'After server reset'
                    }
                },
                'Giant_Wasteland_Basilisk': {
                    'level': 50,
                    'respawn_time': '3 hours',
                    'location': 'Wasteland',
                    'drops': {
                        'epic_chance': '0.8-1.2%',
                        'items': ['Basilisk Belt', 'Speed Boots'],
                        'best_time': 'Low population hours'
                    }
                },
                'Death_Knight': {
                    'level': 55,
                    'respawn_time': '4 hours',
                    'location': 'Giran Territory',
                    'drops': {
                        'epic_chance': '1-1.5%',
                        'items': ['Death Knight Armor', 'Dark Sword'],
                        'best_time': 'Night time spawns'
                    }
                },
                'Cursed_Clara': {
                    'level': 60,
                    'respawn_time': '6 hours',
                    'location': 'Tower of Insolence 3F',
                    'drops': {
                        'epic_chance': '1.5-2%',
                        'items': ['Clara\'s Necklace', 'Magic Ring'],
                        'best_time': 'After maintenance'
                    }
                }
            },
            'elite_field_bosses': {
                'Core': {
                    'level': 65,
                    'respawn_time': '8-12 hours',
                    'location': 'Cruma Tower 3F',
                    'drops': {
                        'epic_chance': '2-3%',
                        'items': ['Core Ring', 'Jewel of Core'],
                        'best_time': 'Random window',
                        'special': 'Requires party'
                    }
                },
                'Orfen': {
                    'level': 70,
                    'respawn_time': '12-24 hours',
                    'location': 'Sea of Spores',
                    'drops': {
                        'epic_chance': '2.5-3.5%',
                        'items': ['Orfen Earring', 'Blessed Scroll'],
                        'best_time': 'Check spawn window',
                        'special': 'Teleports randomly'
                    }
                },
                'Queen_Ant': {
                    'level': 75,
                    'respawn_time': '24-36 hours',
                    'location': 'Ant Nest',
                    'drops': {
                        'epic_chance': '3-4%',
                        'items': ['Queen Ant Ring', 'Royal Armor'],
                        'best_time': 'Scheduled spawn',
                        'special': 'Requires raid party'
                    }
                }
            }
        }
        
        self.world_bosses = {
                'Zaken': {
                    'level': 80,
                    'spawn_schedule': 'Wednesday & Sunday 20:00',
                    'location': 'Devil\'s Isle',
                    'drops': {
                        'epic_chance': '5-8%',
                        'items': ['Zaken Earring', 'Pirate King Sword'],
                        'participation': 'Top 20 damage dealers',
                        'special': 'Server-wide event'
                    }
                },
                'Baium': {
                    'level': 85,
                    'spawn_schedule': 'Saturday 21:00',
                    'location': 'Tower of Insolence Top',
                    'drops': {
                        'epic_chance': '8-10%',
                        'items': ['Baium Ring', 'Angelic Armor'],
                        'participation': 'Top 15 damage dealers',
                        'special': 'Requires special item to spawn'
                    }
                },
                'Antharas': {
                    'level': 90,
                    'spawn_schedule': 'Special events only',
                    'location': 'Dragon Valley',
                    'drops': {
                        'epic_chance': '10-15%',
                        'items': ['Antharas Earring', 'Dragon Slayer'],
                        'participation': 'Top 10 damage dealers',
                        'special': 'Rarest boss'
                    }
                },
                'Valakas': {
                    'level': 95,
                    'spawn_schedule': 'Monthly special event',
                    'location': 'Forge of the Gods',
                    'drops': {
                        'epic_chance': '12-18%',
                        'items': ['Valakas Necklace', 'Fire Dragon Armor'],
                        'participation': 'Top 5 damage dealers',
                        'special': 'Hardest boss'
                    }
                }
        }
        
        # Epic drop rate by day (pattern analysis)
        self.daily_drop_rates = {
            'monday': {
                'modifier': 1.0,
                'reason': 'Standard rates',
                'best_maps': ['Wasteland', 'Orc Barracks']
            },
            'tuesday': {
                'modifier': 1.1,
                'reason': 'Slight boost mid-week',
                'best_maps': ['Cruma Tower', 'Tower of Insolence']
            },
            'wednesday': {
                'modifier': 1.2,
                'reason': 'Maintenance day bonus',
                'best_maps': ['All maps boosted'],
                'special': 'Zaken spawns at 20:00'
            },
            'thursday': {
                'modifier': 1.15,
                'reason': 'Post-maintenance boost',
                'best_maps': ['Ant Nest', 'Sea of Spores']
            },
            'friday': {
                'modifier': 1.05,
                'reason': 'Weekend preparation',
                'best_maps': ['Giran Territory', 'Devil\'s Isle']
            },
            'saturday': {
                'modifier': 1.25,
                'reason': 'Weekend event boost',
                'best_maps': ['All elite zones'],
                'special': 'Baium spawns at 21:00'
            },
            'sunday': {
                'modifier': 1.3,
                'reason': 'Maximum weekend bonus',
                'best_maps': ['World boss zones'],
                'special': 'Zaken spawns at 20:00'
            }
        }
        
        # Map-specific epic drop data
        self.epic_drop_maps = {
            'level_40_50': {
                'Orc_Barracks': {
                    'recommended_level': '45-50',
                    'epic_items': ['Orc Chief Set', 'Warrior Accessories'],
                    'drop_rate': '0.5-1%',
                    'best_time': '02:00-06:00',
                    'mob_density': 'High',
                    'competition': 'Medium'
                },
                'Wasteland': {
                    'recommended_level': '48-52',
                    'epic_items': ['Basilisk Set', 'Speed Items'],
                    'drop_rate': '0.8-1.2%',
                    'best_time': '03:00-07:00',
                    'mob_density': 'Medium',
                    'competition': 'Low'
                }
            },
            'level_50_60': {
                'Giran_Territory': {
                    'recommended_level': '52-58',
                    'epic_items': ['Knight Set', 'Noble Accessories'],
                    'drop_rate': '1-1.5%',
                    'best_time': '00:00-05:00',
                    'mob_density': 'Medium',
                    'competition': 'High'
                },
                'Tower_of_Insolence_1F': {
                    'recommended_level': '55-60',
                    'epic_items': ['Magic Set', 'Wizard Items'],
                    'drop_rate': '1.2-1.8%',
                    'best_time': '04:00-08:00',
                    'mob_density': 'Low',
                    'competition': 'Medium'
                }
            },
            'level_60_70': {
                'Tower_of_Insolence_3F': {
                    'recommended_level': '60-65',
                    'epic_items': ['Clara Set', 'Blessed Items'],
                    'drop_rate': '1.5-2%',
                    'best_time': '02:00-06:00',
                    'mob_density': 'Low',
                    'competition': 'Very High'
                },
                'Cruma_Tower_3F': {
                    'recommended_level': '63-68',
                    'epic_items': ['Core Set', 'Elite Jewels'],
                    'drop_rate': '2-2.5%',
                    'best_time': '03:00-07:00',
                    'mob_density': 'Medium',
                    'competition': 'Very High'
                }
            },
            'level_70_plus': {
                'Sea_of_Spores': {
                    'recommended_level': '70-75',
                    'epic_items': ['Orfen Set', 'Nature Items'],
                    'drop_rate': '2.5-3%',
                    'best_time': '01:00-05:00',
                    'mob_density': 'High',
                    'competition': 'Extreme'
                },
                'Ant_Nest': {
                    'recommended_level': '72-77',
                    'epic_items': ['Queen Set', 'Royal Items'],
                    'drop_rate': '3-3.5%',
                    'best_time': '00:00-04:00',
                    'mob_density': 'Very High',
                    'competition': 'Extreme'
                },
                'Dragon_Valley': {
                    'recommended_level': '75-80',
                    'epic_items': ['Dragon Set', 'Legendary Items'],
                    'drop_rate': '3-4%',
                    'best_time': 'After world boss',
                    'mob_density': 'Medium',
                    'competition': 'Extreme'
                }
            }
        }
    
    def get_current_day_analysis(self):
        """Analyze current day for epic drops"""
        current_day = datetime.now().strftime('%A').lower()
        current_hour = datetime.now().hour
        
        day_data = self.daily_drop_rates.get(current_day, self.daily_drop_rates['monday'])
        
        analysis = {
            'current_day': current_day.capitalize(),
            'drop_modifier': day_data['modifier'],
            'bonus_percentage': f"+{(day_data['modifier']-1)*100:.0f}%",
            'reason': day_data['reason'],
            'recommended_maps': day_data['best_maps'],
            'special_events': day_data.get('special', 'None')
        }
        
        # Time-based recommendations
        if 0 <= current_hour < 6:
            analysis['time_bonus'] = 'EXCELLENT - Low competition'
            analysis['recommended_action'] = 'Farm elite zones now!'
        elif 6 <= current_hour < 12:
            analysis['time_bonus'] = 'GOOD - Moderate competition'
            analysis['recommended_action'] = 'Focus on less popular maps'
        elif 12 <= current_hour < 18:
            analysis['time_bonus'] = 'AVERAGE - Standard competition'
            analysis['recommended_action'] = 'Prepare for evening bosses'
        else:
            analysis['time_bonus'] = 'POOR - High competition'
            analysis['recommended_action'] = 'Wait for late night or join world boss'
        
        return analysis
    
    def get_boss_timers(self):
        """Calculate next boss spawn times"""
        current_time = datetime.now()
        timers = []
        
        # Check world bosses
        for boss_name, boss_data in self.world_bosses.items():
            if 'spawn_schedule' in boss_data:
                schedule = boss_data['spawn_schedule']
                if 'Wednesday' in schedule:
                    next_spawn = self._get_next_weekday(2, 20)  # Wednesday 20:00
                    timers.append({
                        'boss': boss_name,
                        'spawn_time': next_spawn,
                        'time_until': str(next_spawn - current_time).split('.')[0],
                        'drops': boss_data['drops']['items']
                    })
                elif 'Saturday' in schedule:
                    next_spawn = self._get_next_weekday(5, 21)  # Saturday 21:00
                    timers.append({
                        'boss': boss_name,
                        'spawn_time': next_spawn,
                        'time_until': str(next_spawn - current_time).split('.')[0],
                        'drops': boss_data['drops']['items']
                    })
                elif 'Sunday' in schedule:
                    next_spawn = self._get_next_weekday(6, 20)  # Sunday 20:00
                    timers.append({
                        'boss': boss_name,
                        'spawn_time': next_spawn,
                        'time_until': str(next_spawn - current_time).split('.')[0],
                        'drops': boss_data['drops']['items']
                    })
        
        return sorted(timers, key=lambda x: x['spawn_time'])
    
    def _get_next_weekday(self, weekday, hour):
        """Get next occurrence of weekday at specific hour"""
        current = datetime.now()
        days_ahead = weekday - current.weekday()
        
        if days_ahead < 0:  # Target day already happened this week
            days_ahead += 7
        elif days_ahead == 0:  # Target day is today
            if current.hour >= hour:  # Already passed
                days_ahead += 7
        
        target = current + timedelta(days=days_ahead)
        return target.replace(hour=hour, minute=0, second=0, microsecond=0)
    
    def get_recommended_farming_route(self, level):
        """Get recommended farming route based on level"""
        routes = []
        
        if 40 <= level < 50:
            routes = [
                {
                    'priority': 1,
                    'map': 'Orc Barracks',
                    'reason': 'High mob density, decent epic chance',
                    'epic_rate': '0.5-1%',
                    'items': ['Orc Chief Ring', 'Warrior Belt']
                },
                {
                    'priority': 2,
                    'map': 'Wasteland',
                    'reason': 'Lower competition, better rates',
                    'epic_rate': '0.8-1.2%',
                    'items': ['Basilisk Belt', 'Speed Boots']
                }
            ]
        elif 50 <= level < 60:
            routes = [
                {
                    'priority': 1,
                    'map': 'Giran Territory',
                    'reason': 'Death Knight spawns here',
                    'epic_rate': '1-1.5%',
                    'items': ['Death Knight Armor', 'Dark Sword']
                },
                {
                    'priority': 2,
                    'map': 'Tower of Insolence 1F',
                    'reason': 'Good for solo farming',
                    'epic_rate': '1.2-1.8%',
                    'items': ['Magic Set', 'Wizard Items']
                }
            ]
        elif 60 <= level < 70:
            routes = [
                {
                    'priority': 1,
                    'map': 'Tower of Insolence 3F',
                    'reason': 'Cursed Clara spawns',
                    'epic_rate': '1.5-2%',
                    'items': ['Clara\'s Necklace', 'Magic Ring']
                },
                {
                    'priority': 2,
                    'map': 'Cruma Tower 3F',
                    'reason': 'Core spawns, best jewels',
                    'epic_rate': '2-2.5%',
                    'items': ['Core Ring', 'Jewel of Core']
                }
            ]
        else:  # 70+
            routes = [
                {
                    'priority': 1,
                    'map': 'Sea of Spores',
                    'reason': 'Orfen spawns, high value drops',
                    'epic_rate': '2.5-3%',
                    'items': ['Orfen Earring', 'Blessed Scroll']
                },
                {
                    'priority': 2,
                    'map': 'Ant Nest',
                    'reason': 'Queen Ant, best accessories',
                    'epic_rate': '3-3.5%',
                    'items': ['Queen Ant Ring', 'Royal Armor']
                }
            ]
        
        return routes
    
    def calculate_epic_drop_chance(self, base_rate, day_modifier, buffs=None):
        """Calculate actual epic drop chance"""
        final_rate = base_rate * day_modifier
        
        if buffs:
            if 'premium' in buffs:
                final_rate *= 1.2  # 20% premium bonus
            if 'event' in buffs:
                final_rate *= 1.5  # 50% event bonus
            if 'party' in buffs:
                final_rate *= 1.1  # 10% party bonus
        
        return min(final_rate, 10.0)  # Cap at 10%
    
    def generate_daily_report(self):
        """Generate daily epic farming report"""
        report = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'day_analysis': self.get_current_day_analysis(),
            'boss_timers': self.get_boss_timers(),
            'recommended_maps': [],
            'special_notes': []
        }
        
        # Add map recommendations based on day
        current_day = datetime.now().strftime('%A').lower()
        if current_day in ['wednesday', 'saturday', 'sunday']:
            report['special_notes'].append('WORLD BOSS DAY - Prepare for raid!')
        
        if current_day == 'wednesday':
            report['special_notes'].append('Post-maintenance boost active!')
        
        # Time-based recommendations
        current_hour = datetime.now().hour
        if 0 <= current_hour < 6:
            report['recommended_maps'] = ['Tower of Insolence 3F', 'Cruma Tower 3F']
            report['special_notes'].append('Prime farming time - Low competition!')
        elif 19 <= current_hour <= 22:
            report['special_notes'].append('Check for world boss spawns!')
        
        return report

# This class will be integrated into the main optimizer