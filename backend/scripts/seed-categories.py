import time
from django.db import transaction
from app.services.models import MainCategory, SubCategory

catagories = [
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_95_180523_143649_64660dd1de755.png",
        "category_id": "95",
        "category_image": "https://srvme.com/image/data/service_noimage.png",
        "category_name_ar": "عقد صيانة سنوي",
        "category_name_en": "Maintenance Contract",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": {
            "62": "Ac Maintenance Contract"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_9_240123_100152_63cf82603c219.png",
        "category_id": "9",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_9_250123_104113_63d0dd1916737.png",
        "category_name_ar": "اجهزة منزلية",
        "category_name_en": "Appliances Repair",
        "offer_list": [],
        "offers_position": "top",
        "service_list": {
            "40": "General Appliances Repair",
            "41": "Refrigerator & Freezer Repair",
            "42": "Stove & Oven Repair",
            "43": "Washer Or Dryer Cleaning",
            "44": "Water Dispenser Repair",
            "254": "Dishwasher Repair",
            "257": "Ice Maker",
            "389": "Gas Burner Cleaning",
            "392": "Washer Or Dryer Repair",
            "393": "Washer And Dryer Cleaning"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_14_220123_103028_63cce6144607d.png",
        "category_id": "14",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_14_250123_110218_63d0e20a48c3b.png",
        "category_name_ar": "التكييف والتهوية المركزية",
        "category_name_en": "Air Conditioning & Ventilation",
        "offer_list": {
            "30": "6 Mini Split For Only 35 Kd",
            "33": "Wash 8 Packge Units For Only 38 Kd",
            "36": "Wash 6 Dx Units For Only 45 Kd",
            "37": "Wash 8 Dx Units For Only 55 Kd",
            "38": "Wash 2 Dx Units For Only 15 Kd",
            "40": "Wash 8 Mini Split For Only 45 Kd",
            "95": "Wash 6 Packge Units For Only 29 Kd",
            "96": "Wash 2 Package Units For Only 10 Kd",
            "98": "Wash 2 Mini Split For Only 12 Kd",
            "99": "Deep Cleaning For 3 Mini Splits With Plastic",
            "101": "Deep Cleaning For Mini Split With Plastic She",
            "102": "Special Cleaning For Mini Split With Plastic"
        },
        "offers_position": "top",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "52",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_52_250123_113004_63d0e88cdd2e8.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_52_250123_113004_63d0e88cde0b6.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "2": "Thermostat Replacement",
                    "12": "Central A/c Repair",
                    "13": "Central A/c Cleaning",
                    "235": "Central A/c Replacement",
                    "301": "Central A/c Duct Cleaning",
                    "330": "Gas Leak Repair",
                    "331": "Capacitor Replacement"
                },
                "category_name_en": "Central A/c",
                "category_name_ar": "تكييف مركزى"
            },
            {
                "category_id": "53",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_53_250123_125021_63d0fb5de3787.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_53_250123_125021_63d0fb5de4369.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "214": "Mini Split Repair",
                    "215": "Mini Split Cleaning",
                    "216": "Mini Split Gas Leak Repair",
                    "310": "Mini Split Capacitor Replacement",
                    "332": "Pc Board Replacement"
                },
                "category_name_en": "Mini Split A/c",
                "category_name_ar": "وحدات تكييف"
            },
            {
                "category_id": "8",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_8_240123_080628_63cf675477b90.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_8_250123_125225_63d0fbd9eb7ae.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "22": "Installing & Repairing Kitchen Hood",
                    "23": "General Ventilation Repair",
                    "253": "Installing New Kitchen Hood Or Fan"
                },
                "category_name_en": "Ventilation",
                "category_name_ar": "تهوية و شفاطات "
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_6_230123_065316_63ce04acd7fb3.png",
        "category_id": "6",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_6_250123_105134_63d0df86bed46.png",
        "category_name_ar": "كهربائي",
        "category_name_en": "Electrical",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": {
            "3": "Light Bulb Replacement",
            "4": "Replacing Mini Circuit Breaker",
            "19": "Outlets & Switches Replacement",
            "20": "General Electrical Repair",
            "348": "Replacing Main Circuit Breaker",
            "349": "New Power Outlet Installation",
            "350": "Chandelier Installation",
            "351": "New Lighting Point Installation",
            "352": "Short Circuit Repair",
            "353": "Light Fixture Installation",
            "415": "Smoke Detectors"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_86_250123_111247_63d0e47fb404c.png",
        "category_id": "86",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_86_250123_111247_63d0e47fb4bae.png",
        "category_name_ar": "عازل الأسطح",
        "category_name_en": "Roof Insulation",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": {
            "295": "Roof Insulation Assessment"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_2_220123_102817_63cce591e9052.png",
        "category_id": "2",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_2_250123_111139_63d0e43b064ed.png",
        "category_name_ar": "صحي",
        "category_name_en": "Plumbing",
        "offer_list": [],
        "offers_position": "top",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "114",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_114_250123_114021_63d0eaf528193.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_114_250123_114021_63d0eaf528d73.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "14": "Drain Cleaning Assessment",
                    "396": "Drain Jack Unclogging",
                    "397": "Drain Unclogging With Spring Machine",
                    "398": "Toilet Unclogging",
                    "403": "Sink Or Shower Unclogging"
                },
                "category_name_en": "Drain Cleaning",
                "category_name_ar": "تسليك البواليع "
            },
            {
                "category_id": "121",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_121_220623_123613_6494160d0e571.png",
                "category_image": "https://srvme.com/image/data/service_noimage.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "17": "Plumbing Assessment",
                    "270": "Washing Machine Installation Or Relocation"
                },
                "category_name_en": "General Plumbing Repair",
                "category_name_ar": "إصلاحات عامة وتركيبات للصرف الصحي"
            },
            {
                "category_id": "108",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_108_230123_072520_63ce0c306e4ee.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_108_250123_130529_63d0fee952d05.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "357": "Valve Replacement",
                    "358": "Sink Accessories Installation",
                    "359": "Sink Component Installation",
                    "360": "Sink Replacement",
                    "361": "Mixer Installation",
                    "362": "Shower Stand Installation",
                    "405": "Bathtub Installation Or Replacement"
                },
                "category_name_en": "Sink And Shower",
                "category_name_ar": "المغسله والشاور "
            },
            {
                "category_id": "109",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_109_220623_123343_6494157725eaf.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_109_250123_130647_63d0ff3708d3e.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "363": "Float Replacement",
                    "364": "Toilet Cover Installation",
                    "365": "Valve Installation",
                    "366": "Water Hose Replacement",
                    "367": "Toilet Mixer Replacement",
                    "368": "Toilet Leak Repair",
                    "369": "Toilet Removal & Installation",
                    "404": "Toilet Flush Repair"
                },
                "category_name_en": "Toilet",
                "category_name_ar": "المرحاض"
            },
            {
                "category_id": "111",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_111_250123_125122_63d0fb9a7ef20.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_111_230123_072800_63ce0cd0877ce.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "372": "Central Water Filters Maintenance Or Replacement",
                    "399": "Transparent Water Filter Maintenance",
                    "400": "Ceramic Water Filter Maintenance",
                    "401": "Transparent Water Filter Installation Or Replacement",
                    "402": "Ceramic Water Filter Installation Or Replacement"
                },
                "category_name_en": "Water Filter",
                "category_name_ar": "فلاتر المياه"
            },
            {
                "category_id": "28",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_28_240123_081538_63cf697a7bb07.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_28_250123_113315_63d0e94b9ebfc.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "5": "Boiler Replacement",
                    "85": "Central Heater Maintenance",
                    "86": "Central Heater Replacement",
                    "406": "Heater Component Replacement"
                },
                "category_name_en": "Water Heater",
                "category_name_ar": "سخان المياه"
            },
            {
                "category_id": "113",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_113_230123_072827_63ce0ceb11de5.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_113_250123_124609_63d0fa6111472.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "16": "Water Pump Replacement",
                    "371": "Water Pump Maintenance"
                },
                "category_name_en": "Water Pump",
                "category_name_ar": "مضخات المياه"
            },
            {
                "category_id": "112",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_112_250123_124509_63d0fa250e9fa.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_112_250123_124509_63d0fa250f501.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "300": "Water Tank Cleaning",
                    "370": "Water Tank & Pipes Assessment"
                },
                "category_name_en": "Water Tanks And Pipes",
                "category_name_ar": "خزانات المياه والبايبات"
            },
            {
                "category_id": "115",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_115_230123_073805_63ce0f2da5502.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_115_230123_073805_63ce0f2da6112.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "21": "Installing Toilet Glass Fan"
                },
                "category_name_en": "Window Fan",
                "category_name_ar": "شفاط النافذة"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_90_250123_110133_63d0e1dd6549c.png",
        "category_id": "90",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_90_250123_110133_63d0e1dd660b6.png",
        "category_name_ar": "عامل متكامل",
        "category_name_en": "Handyman",
        "offer_list": {
            "115": "Roller Curtains Installation"
        },
        "offers_position": "bottom",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "88",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_88_250123_112303_63d0e6e74285a.png",
                "category_image": "https://srvme.com/image/data/service_noimage.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "321": "Baby Box",
                    "323": "Baby Proofing Assessment",
                    "336": "Toddler Box",
                    "337": "Preschool Box",
                    "391": "Furniture Strap"
                },
                "category_name_en": "Baby Proofing",
                "category_name_ar": "خدمة حماية الاطفال"
            },
            {
                "category_id": "118",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_118_230123_074310_63ce105e57b05.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_118_250123_113703_63d0ea2f51fcf.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "387": "Installation Of Small/medium Size Curtains",
                    "388": "Installing Large Curtains"
                },
                "category_name_en": "Curtains Installation",
                "category_name_ar": "تعليق ستائر "
            },
            {
                "category_id": "117",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_117_220623_123903_649416b751ea1.png",
                "category_image": "https://srvme.com/image/data/service_noimage.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "384": "Small Frame",
                    "385": "Medium Frame",
                    "386": "Large Frame"
                },
                "category_name_en": "Frame Installation",
                "category_name_ar": "تعليق لوحات "
            },
            {
                "category_id": "126",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_126_170424_125218_661f9bd250daf.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_126_170424_125218_661f9bd252318.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "414": "Handyman Assessment"
                },
                "category_name_en": "General Handyman Repair",
                "category_name_ar": "معاينة عامل متكامل "
            },
            {
                "category_id": "119",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_119_250123_125512_63d0fc80a1a09.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_119_250123_125512_63d0fc80a256a.png",
                "offers_position": "top",
                "sub_category": [],
                "service_list": {
                    "318": "Mirror  Installation - Large Size"
                },
                "category_name_en": "Mirror",
                "category_name_ar": "مرايا"
            },
            {
                "category_id": "116",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_116_250123_130356_63d0fe8c9aabc.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_116_250123_130356_63d0fe8c9b587.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "381": "Small Shelf",
                    "382": "Medium Shelf",
                    "383": "Large Shelf"
                },
                "category_name_en": "Shelves Installation",
                "category_name_ar": "تعليق أرفف"
            },
            {
                "category_id": "120",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_120_250123_125433_63d0fc5945573.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_120_250123_125433_63d0fc5946109.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "315": "Tv Mounting",
                    "316": "Tv Dismounting & Remounting"
                },
                "category_name_en": "Tv",
                "category_name_ar": "تلفاز"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_3_230123_065029_63ce040559a0a.png",
        "category_id": "3",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_3_250123_104502_63d0ddfe606d3.png",
        "category_name_ar": "نجار",
        "category_name_en": "Carpenter",
        "offer_list": [],
        "offers_position": "top",
        "service_list": {
            "8": "New Design & Workshop",
            "18": "General Carpenter Repair",
            "322": "Wooden Waste Bin Box",
            "390": "Tv Wall Unit"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_102_250123_105948_63d0e174bbfb4.png",
        "category_id": "102",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_102_250123_105948_63d0e174bca93.png",
        "category_name_ar": "مقاولات عامة",
        "category_name_en": "General Contractor",
        "offer_list": [],
        "offers_position": "top",
        "service_list": {
            "342": "General Contractor"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_43_220123_162830_63cd39fe8e99f.png",
        "category_id": "43",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_43_250123_104913_63d0def9d68a9.png",
        "category_name_ar": "ستائر وتنجيد",
        "category_name_en": "Curtains & Upholstery",
        "offer_list": [],
        "offers_position": "top",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "44",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_44_240123_094846_63cf7f4e0aa31.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_44_250123_114132_63d0eb3c909fd.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "156": "1 Line Curtains",
                    "157": "2 Lines Curtains",
                    "158": "3 Lines Curtains",
                    "159": "Curtains Maintenance"
                },
                "category_name_en": "Fabric Curtains",
                "category_name_ar": "ستاير خام"
            },
            {
                "category_id": "45",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_45_250123_125950_63d0fd96a33fe.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_45_250123_125950_63d0fd96a4126.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "160": "Roller Curtains Fabrication & Installation"
                },
                "category_name_en": "Roller Curtains",
                "category_name_ar": "ستائر رول "
            },
            {
                "category_id": "99",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_99_240123_095113_63cf7fe1427e3.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_99_230123_074544_63ce10f8c532f.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "334": "Sofa Maintenance",
                    "335": "New Sofa Design"
                },
                "category_name_en": "Upholstery",
                "category_name_ar": "تنجيد"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_93_230123_064946_63ce03da51a5d.png",
        "category_id": "93",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_93_250123_104428_63d0dddc33516.png",
        "category_name_ar": "خدمة السيارات",
        "category_name_en": "Car Services",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "10",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_10_250123_112632_63d0e7b85ec19.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_10_250123_112632_63d0e7b85f9ec.png",
                "offers_position": "top",
                "sub_category": [],
                "service_list": {
                    "31": "Flat Tire Repair",
                    "32": "Battery Recharge",
                    "36": "Tire Replacement",
                    "153": "Battery Replacement",
                    "187": "Oil & Filter Replacement",
                    "217": "Brake Pads Change",
                    "218": "Disc Trimming",
                    "220": "Ac Gas Filling",
                    "221": "Rims Trimming",
                    "255": "General Maintenance",
                    "256": "Suspension Works"
                },
                "category_name_en": "Car Repair",
                "category_name_ar": "صيانة سيارات"
            },
            {
                "category_id": "62",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_62_240123_083445_63cf6df51314a.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_62_250123_112658_63d0e7d2dd7e0.png",
                "offers_position": "bottom",
                "sub_category": [
                    {
                        "category_id": "64",
                        "category_name": "5 Seaters",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_64_240123_083514_63cf6e1254856.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_64_250123_124111_63d0f9372894f.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "240": "Wash For 5 Seaters",
                            "242": "Shine For 5 Seaters",
                            "244": "Detailing For 5 Seaters"
                        }
                    },
                    {
                        "category_id": "65",
                        "category_name": "7 Seaters",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_65_240123_083529_63cf6e21c6f4c.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_65_250123_124034_63d0f91284146.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "241": "Wash For 7 Seaters",
                            "243": "Shine For 7 Seaters",
                            "245": "Detailing For 7 Seaters"
                        }
                    },
                    {
                        "category_id": "63",
                        "category_name": "Sedan",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_63_240123_083557_63cf6e3d073ee.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_63_250123_120906_63d0f1b26457a.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "237": "Wash",
                            "238": "Shine",
                            "239": "Detailing"
                        }
                    }
                ],
                "service_list": [],
                "category_name_en": "Car Wash",
                "category_name_ar": "غسيل السيارات"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_17_250123_104004_63d0dcd4265bf.png",
        "category_id": "17",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_17_250123_104004_63d0dcd427777.png",
        "category_name_ar": "ألومنيوم وشتر",
        "category_name_en": "Aluminum & Shutter",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "70",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_70_240123_083731_63cf6e9b6c13d.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_70_250123_111715_63d0e58b31db3.png",
                "offers_position": "bottom",
                "sub_category": [
                    {
                        "category_id": "73",
                        "category_name": "Aluminum Cabinets",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_73_240123_083833_63cf6ed9929e9.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_73_250123_123959_63d0f8ef67624.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "50": "General Cabinets Repair"
                        }
                    },
                    {
                        "category_id": "71",
                        "category_name": "Aluminum Door",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_71_240123_083846_63cf6ee64babd.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_71_250123_123941_63d0f8ddb787a.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "48": "Aluminum Door Repair",
                            "260": "Handle Replacement",
                            "261": "Door Handle Replacement",
                            "262": "Door Hinges Replacement",
                            "299": "Door Fly Screen Replacement"
                        }
                    },
                    {
                        "category_id": "89",
                        "category_name": "Aluminum Waste Bin Cover",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_89_250123_123910_63d0f8beb601a.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_89_240123_083910_63cf6efe2d1c3.png",
                        "offers_position": "top",
                        "service_list": {
                            "312": "Waste Bin Cover Box"
                        }
                    },
                    {
                        "category_id": "72",
                        "category_name": "Aluminum Window",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_72_240123_084132_63cf6f8c671f9.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_72_250123_123651_63d0f8332b706.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "49": "Aluminum Windows Repair",
                            "53": "General Windows Repair",
                            "263": "Window Hinges Replacement",
                            "264": "Windows Handle Replacement",
                            "298": "Window Fly Screen Replacement"
                        }
                    }
                ],
                "service_list": [],
                "category_name_en": "Aluminum",
                "category_name_ar": "الألومنيوم"
            },
            {
                "category_id": "69",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_69_240123_083748_63cf6eac61bd2.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_69_250123_130502_63d0fececdfab.png",
                "offers_position": "bottom",
                "sub_category": [
                    {
                        "category_id": "74",
                        "category_name": "Automatic Shutter",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_74_250123_123417_63d0f799c2eaf.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_74_250123_123417_63d0f799c3a6b.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "51": "Automatic Shutter Repair",
                            "165": "New Shutter Installation"
                        }
                    },
                    {
                        "category_id": "75",
                        "category_name": "Manual Shutter",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_75_250123_122641_63d0f5d1b75eb.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_75_250123_122641_63d0f5d1b81c4.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "52": "Manual Shutter Repair",
                            "258": "New Manual Shutter Installation"
                        }
                    }
                ],
                "service_list": [],
                "category_name_en": "Shutter",
                "category_name_ar": "شتر"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_5_250123_110950_63d0e3cecae47.png",
        "category_id": "5",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_5_250123_110950_63d0e3cecb8d6.png",
        "category_name_ar": "صبغ و ورق جدران",
        "category_name_en": "Painting & Wallpaper",
        "offer_list": [],
        "offers_position": "top",
        "service_list": {
            "7": "Interior Painting",
            "9": "Wood Painting",
            "10": "General Painting Repair",
            "11": "Wallpaper"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_98_250123_110834_63d0e382674c8.png",
        "category_id": "98",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_98_250123_110834_63d0e3826803a.png",
        "category_name_ar": "خدمة النقل",
        "category_name_en": "Moving & Shifting",
        "offer_list": [],
        "offers_position": "top",
        "service_list": {
            "327": "Flat Moving",
            "328": "House Moving",
            "329": "Office Moving"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_80_220123_162906_63cd3a22795e9.png",
        "category_id": "80",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_80_250123_105852_63d0e13ce39d1.png",
        "category_name_ar": "حدائق",
        "category_name_en": "Gardening",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "122",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_122_270823_104617_64eaff49dc0d3.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_122_270823_104617_64eaff49dcedb.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "284": "Designing New Garden"
                },
                "category_name_en": "Garden Design",
                "category_name_ar": "تصميم حدائق"
            },
            {
                "category_id": "81",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_81_230123_075142_63ce125e2525a.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_81_250123_114253_63d0eb8dddbb6.png",
                "offers_position": "bottom",
                "sub_category": [
                    {
                        "category_id": "92",
                        "category_name": "Flowers",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_92_250123_123349_63d0f77d745ba.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_92_250123_123349_63d0f77d74ff8.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "272": "Planting Flowers"
                        }
                    },
                    {
                        "category_id": "84",
                        "category_name": "Grass Installation",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_84_250123_123309_63d0f755405a8.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_84_250123_123309_63d0f755411da.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "271": "Agricultural Soil",
                            "275": "Artificial Grass",
                            "276": "Natural Grass"
                        }
                    },
                    {
                        "category_id": "83",
                        "category_name": "Irrigation System",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_83_091123_103952_654c8cc8eb526.png",
                        "category_image": "https://srvme.com/image/data/service_noimage.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "274": "Manual Irrigation System",
                            "286": "Automatic Irrigation System"
                        }
                    },
                    {
                        "category_id": "94",
                        "category_name": "Maintenance & Assessments",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_94_250123_122806_63d0f626294c9.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_94_250123_122806_63d0f62629fd8.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "273": "Planting Trees",
                            "285": "Gardening Maintenance Assessments"
                        }
                    },
                    {
                        "category_id": "85",
                        "category_name": "Palm Trees",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_85_250123_121718_63d0f39e13b2d.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_85_250123_121718_63d0f39e1465c.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "277": "Planting New Palm Tree",
                            "278": "Pollination",
                            "279": "Date Moth & Spider Spray",
                            "280": "Dates Bagging",
                            "281": "Bending Of Branches",
                            "282": "Fertilization",
                            "283": "Picking Of Dates"
                        }
                    }
                ],
                "service_list": [],
                "category_name_en": "Garden Maintenance",
                "category_name_ar": "صيانة الحدائق"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_46_240123_140709_63cfbbdda7620.png",
        "category_id": "46",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_46_250123_110423_63d0e287ecca7.png",
        "category_name_ar": "مفاتيح واقفال",
        "category_name_en": "Locksmith",
        "offer_list": [],
        "offers_position": "top",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "125",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_125_170124_150620_65a7c2bcee4be.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_125_170124_150620_65a7c2bceeec6.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "30": "General Locksmith Repair",
                    "161": "Iseo Italian Cylinder Replacement",
                    "162": "Unlock Door & Change Regular Cylinder",
                    "297": "Lock Cylinder Replacement",
                    "307": "Unlock Door & Change Iseo Italian Cylinder",
                    "308": "Regular Lock Cylinder Replacement",
                    "309": "Iseo Italian Lock Replacement",
                    "394": "Window Handle Lock"
                },
                "category_name_en": "Regular Locks",
                "category_name_ar": "اقفال منازل"
            },
            {
                "category_id": "124",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_124_210124_093810_65acbbd2d92ac.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_124_170124_145657_65a7c0896b834.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "409": "Smart Door Lock Installation",
                    "410": "Smart Lock For Wooden Door",
                    "411": "Smart Lock For Aluminium Door",
                    "412": "Smart Lock For Glass Door"
                },
                "category_name_en": "Smart Locks",
                "category_name_ar": "أقفال الكترونية"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_22_250123_104752_63d0dea86bcab.png",
        "category_id": "22",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_22_250123_105916_63d0e15446de3.png",
        "category_name_ar": "تنظيف و تعقيم ",
        "category_name_en": "Cleaning & Sanitization",
        "offer_list": [],
        "offers_position": "top",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "16",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_16_240123_074831_63cf631f183ef.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_16_250123_113549_63d0e9e52b7d7.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "67": "Exterior Facade",
                    "68": "Kitchen Hood Cleaning",
                    "69": "Apartment Cleaning",
                    "70": "Furniture Cleaning",
                    "71": "Carpet Cleaning",
                    "72": "Floor Cleaning",
                    "225": "General Cleaning",
                    "269": "Kitchen Cleaning",
                    "302": "Duct Cleaning",
                    "413": "Stove & Oven Cleaning"
                },
                "category_name_en": "Cleaning",
                "category_name_ar": "تنظيف"
            },
            {
                "category_id": "47",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_47_250123_130226_63d0fe325fdb1.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_47_250123_130138_63d0fe0216435.png",
                "offers_position": "top",
                "sub_category": [],
                "service_list": {
                    "163": "House Sanitization",
                    "164": "Office Sanitization",
                    "166": "Furniture Sanitization",
                    "184": "Car Sanitization"
                },
                "category_name_en": "Sanitization",
                "category_name_ar": "تعقيم"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_13_240123_140614_63cfbba647528.png",
        "category_id": "13",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_13_250123_105736_63d0e0f079788.png",
        "category_name_ar": "تركيب اثاث",
        "category_name_en": "Furniture Assembly",
        "offer_list": [],
        "offers_position": "top",
        "service_list": {
            "26": "Queen/king Bed",
            "27": "Furniture Installation & Reassembling",
            "28": "Single Bed",
            "152": "General Furniture Assembly",
            "373": "Chair",
            "374": "Tv Table",
            "375": "Desk",
            "376": "Single Door Closet",
            "377": "2 Door Closet",
            "378": "4 Door Closet",
            "379": "6 Door Closet",
            "380": "8 Doors Closet"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_25_220123_163041_63cd3a817a045.png",
        "category_id": "25",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_25_250123_110638_63d0e30e77524.png",
        "category_name_ar": "صيانة موبايلات",
        "category_name_en": "Mobile Repair",
        "offer_list": [],
        "offers_position": "top",
        "service_list": {
            "179": "Other Mobile Screens"
        },
        "sub_category": [
            {
                "category_id": "26",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_26_240123_090308_63cf749c0eba3.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_26_250123_112116_63d0e67c1fe2c.png",
                "offers_position": "bottom",
                "sub_category": [
                    {
                        "category_id": "32",
                        "category_name": "Apple Watch Repair",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_32_240123_090321_63cf74a9b9826.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_32_250123_123500_63d0f7c500446.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "117": "Touch Screen Series 3",
                            "118": "Touch Screen Series 4",
                            "119": "Touch Screen Series 5",
                            "325": "Touch Screen Series 6"
                        }
                    },
                    {
                        "category_id": "36",
                        "category_name": "Ipad Screens",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_36_250123_124150_63d0f95e432cb.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_36_250123_124150_63d0f95e43e26.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "120": "Ipad 2/3/4 Lcd",
                            "121": "Ipad Mini 4 Lcd",
                            "123": "Ipad Air Lcd",
                            "126": "Ipad Air 2 Lcd",
                            "127": "Ipad Mini 3 Lcd",
                            "171": "Other Ipad Lcd's",
                            "203": "Ipad Air 4 Lcd",
                            "204": "Ipad Air 3 Lcd"
                        }
                    },
                    {
                        "category_id": "27",
                        "category_name": "Iphone Batteries",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_27_250123_122934_63d0f67ee0fa9.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_27_250123_122934_63d0f67ee1fb1.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "91": "Iphone 8 Battery",
                            "92": "Iphone 7/7+ Battery",
                            "93": "Iphone 8+ Battery",
                            "94": "Iphone X/xs Battery",
                            "95": "Iphone X Max Battery",
                            "96": "Iphone Xr Battery",
                            "168": "Other Iphone Batteries"
                        }
                    },
                    {
                        "category_id": "66",
                        "category_name": "Iphone Screens",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_66_250123_122902_63d0f65e1b97f.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_66_250123_122902_63d0f65e1d72b.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "76": "Iphone Xs Max Screen",
                            "77": "Iphone 7 Screen",
                            "81": "Iphone 6s/6s+ Screen",
                            "82": "Iphone 8+ Screen",
                            "83": "Iphone Xr Screen",
                            "84": "Iphone Xs Screen",
                            "87": "Iphone 7+ Screen",
                            "88": "Iphone 8 Screen",
                            "89": "Iphone X Screen",
                            "167": "Other Iphone Screens",
                            "173": "Iphone 11 Screen",
                            "174": "Iphone 11 Pro Screen",
                            "175": "Iphone 11 Pro Max Screen",
                            "191": "Iphone 12 Pro Screen",
                            "194": "Iphone 12 Pro Max Screen",
                            "207": "Iphone 12 Screen"
                        }
                    }
                ],
                "service_list": {
                    "344": "Other Mobile Repairs"
                },
                "category_name_en": "Apple",
                "category_name_ar": "ابل "
            },
            {
                "category_id": "48",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_48_240123_090356_63cf74cce95f6.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_48_250123_125536_63d0fc987b8b4.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "180": "Other Mobile Batteries"
                },
                "category_name_en": "Other Repairs",
                "category_name_ar": "إصلاحات أخرى"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_55_250123_105645_63d0e0bd9999c.png",
        "category_id": "55",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_55_250123_105645_63d0e0bd9a4a4.png",
        "category_name_ar": "أرضيات ",
        "category_name_en": "Flooring",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "56",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_56_250123_113521_63d0e9c9259b1.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_56_250123_113521_63d0e9c926456.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "226": "Remove Old & Install New Ceramic",
                    "227": "Ceramic Assessment",
                    "234": "New Ceramic Installation"
                },
                "category_name_en": "Ceramic Installation",
                "category_name_ar": "تركيب سيراميك"
            },
            {
                "category_id": "57",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_57_250123_114339_63d0ebbb61777.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_57_250123_114339_63d0ebbb62378.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "228": "New Marble Installation",
                    "229": "Remove Old & Install New Marble",
                    "230": "Marble Assessment"
                },
                "category_name_en": "Marble Installation",
                "category_name_ar": "تركيب رخام"
            },
            {
                "category_id": "58",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_58_250123_125845_63d0fd5551323.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_58_250123_125845_63d0fd5551e35.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "231": "New Parquet Installation",
                    "232": "Remove Old & Install New Parquet",
                    "233": "Parquet Assessment"
                },
                "category_name_en": "Parquet Installation",
                "category_name_ar": "تركيب باركيه"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_7_230123_070004_63ce0644b7f3d.png",
        "category_id": "7",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_7_250123_111630_63d0e55e8e087.png",
        "category_name_ar": "التلفزيون و الستلايت ",
        "category_name_en": "Tv & Satellite",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": {
            "6": "Tv Installation",
            "24": "Central Satellite Maintenance & Repair",
            "25": "Tv & Satellite Assessment",
            "247": "Lnb Installation",
            "248": "Receiver Programming",
            "249": "Smart Tv Programing",
            "250": "New Dish Installation",
            "251": "Osn Service",
            "252": "Osn Installation & Programing"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_24_230123_065157_63ce045d5555b.png",
        "category_id": "24",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_24_250123_105022_63d0df3e19ac2.png",
        "category_name_ar": "ديكور وجبس بورد",
        "category_name_en": "Decor & Gypsum Board",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": {
            "73": "Gypsum Board Installation",
            "74": "Decor Installation",
            "267": "Decor Maintenance",
            "268": "Gypsum Board Maintenance"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_79_220123_163148_63cd3ac4eef4f.png",
        "category_id": "79",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_79_250123_110009_63d0e18999ffc.png",
        "category_name_ar": "أعمال الزجاج و لوح الحائط",
        "category_name_en": "Glass Works & Wall Board",
        "offer_list": {
            "114": "Acrylic Board With Design"
        },
        "offers_position": "bottom",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "123",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_123_240923_132901_65100f6d57f0d.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_123_200923_083639_650a84e74406a.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "287": "Glass Maintenance",
                    "288": "Glass Shelves",
                    "289": "Glass Shower Box",
                    "290": "Glass Table Tops",
                    "291": "Glass Railing",
                    "292": "Glass Mirrors",
                    "293": "Glass Doors",
                    "294": "Glass Facade"
                },
                "category_name_en": "Glass Work",
                "category_name_ar": "أعمال الزجاج"
            },
            {
                "category_id": "106",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_106_240923_132851_65100f630384e.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_106_240123_080133_63cf662de197b.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "346": "Acrylic Board With Design",
                    "347": "Acrylic Board Without Design",
                    "407": "Designing New Wall Board"
                },
                "category_name_en": "Wall Board",
                "category_name_ar": "لوح حائط"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_30_220123_163218_63cd3ae2f3777.png",
        "category_id": "30",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_30_250123_105324_63d0dff4ca2c6.png",
        "category_name_ar": "الكترونيات",
        "category_name_en": "Electronic Repair",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "91",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_91_240123_081150_63cf6896ed678.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_91_250123_113611_63d0e9fb6e58a.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "129": "Windows Format & Installation",
                    "130": "Mac Format & Installation",
                    "224": "General Computers & Laptops Repair"
                },
                "category_name_en": "Computers & Laptops",
                "category_name_ar": "كمبيوتر ولاب توب"
            },
            {
                "category_id": "29",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_29_240123_091443_63cf775321193.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_29_250123_125201_63d0fbc15e467.png",
                "offers_position": "bottom",
                "sub_category": [
                    {
                        "category_id": "38",
                        "category_name": "Ps4",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_38_250123_121236_63d0f2846278a.png",
                        "category_image": "https://srvme.com/image/data/service_noimage.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "131": "Hdmi",
                            "132": "Cd Drive Lens",
                            "133": "Cd Rom",
                            "135": "Software Update",
                            "136": "Hard Disk 500gb",
                            "137": "Hard Disk 1000gb"
                        }
                    },
                    {
                        "category_id": "39",
                        "category_name": "Xbox",
                        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_39_250123_120819_63d0f1833f25c.png",
                        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_39_250123_120819_63d0f1833fe67.png",
                        "offers_position": "bottom",
                        "service_list": {
                            "138": "Hdmi Xbox",
                            "139": "Hard Disk 1000gb Xbox",
                            "140": "Hard Disk 500gb Xbox",
                            "141": "Cd Drive Lens Xbox",
                            "142": "Cd Rom Xbox",
                            "144": "Software Update Xbox"
                        }
                    }
                ],
                "service_list": [],
                "category_name_en": "Video Games Repair",
                "category_name_ar": "تصليح ألعاب الفيديو"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_76_220123_163300_63cd3b0c7ea9a.png",
        "category_id": "76",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_76_250123_110526_63d0e2c6a047b.png",
        "category_name_ar": "خدمة الحديد والمظلات",
        "category_name_en": "Metal Works & Shades",
        "offer_list": [],
        "offers_position": "top",
        "service_list": [],
        "sub_category": [
            {
                "category_id": "101",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_101_240123_075443_63cf64936633e.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_101_250123_114453_63d0ec058b456.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "338": "Metal Handrail",
                    "339": "Metal Fences",
                    "340": "Metal Doors",
                    "341": "Special Designs",
                    "345": "General Metal Repair"
                },
                "category_name_en": "Metal Works",
                "category_name_ar": "أعمال الحديد"
            },
            {
                "category_id": "100",
                "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_100_240123_075509_63cf64ad0bbcf.png",
                "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_100_250123_125758_63d0fd267d2c0.png",
                "offers_position": "bottom",
                "sub_category": [],
                "service_list": {
                    "265": "New Parking Shades Installation",
                    "266": "Parking Shades Maintenance"
                },
                "category_name_en": "Parking Shades",
                "category_name_ar": "المظلات"
            }
        ]
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_15_230123_064924_63ce03c49562f.png",
        "category_id": "15",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_15_250123_104159_63d0dd474c54b.png",
        "category_name_ar": "كاميرات",
        "category_name_en": "Cameras",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": {
            "45": "Cameras Maintenance",
            "46": "Cameras Installation"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_87_230123_065227_63ce047b55863.png",
        "category_id": "87",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_87_250123_105058_63d0df6204f5c.png",
        "category_name_ar": "خدمة الدكتات",
        "category_name_en": "Ducting Service",
        "offer_list": [],
        "offers_position": "bottom",
        "service_list": {
            "304": "Supply & Install New Air Vent",
            "305": "Replace Duct Canvas Or Insulation",
            "306": "Modify Existing Duct Work",
            "333": "Air Filter Replacement"
        },
        "sub_category": []
    },
    {
        "category_icon": "https://srvme.com/image/data/categoryIcon/categoryIcon_19_250123_111033_63d0e3f90dac5.png",
        "category_id": "19",
        "category_image": "https://srvme.com/image/data/categoryImage/categoryImage_19_250123_111033_63d0e3f90e7f2.png",
        "category_name_ar": "مكافحة الحشرات",
        "category_name_en": "Pest Control",
        "offer_list": {
            "51": "Get Rid Of Cockroaches & Ants"
        },
        "offers_position": "top",
        "service_list": {
            "54": "Bed Bug Spray",
            "55": "Birds Control",
            "56": "Cockroaches Spray",
            "57": "Rodents Control",
            "58": "White Ant Spray",
            "66": "Weevil Insect Control",
            "408": "General Pest Control"
        },
        "sub_category": []
    }
]

def run():
    start_time = time.time()
    # start a transaction
    transaction.set_autocommit(False)

    MainCategory.objects.bulk_create(
        [
            MainCategory(
                id=category["category_id"],
                name_en=category["category_name_en"],
                name_ar=category["category_name_ar"],
                icon=category["category_icon"],
            )
            for category in catagories
        ]
    )

    SubCategory.objects.bulk_create(
        [
            SubCategory(
                id=sub_category["category_id"],
                name_en=sub_category["category_name_en"],
                name_ar=sub_category["category_name_ar"],
                icon=sub_category["category_icon"],
                parent_id=category["category_id"],
            )
            for category in catagories
            for sub_category in category["sub_category"]
        ]
    )

    transaction.commit()

    print(f"Time taken: {time.time() - start_time} seconds")