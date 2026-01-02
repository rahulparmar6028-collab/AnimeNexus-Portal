# data.py

ANIME_DB = {
    "Naruto": [
        {"type": "Series", "title": "Naruto (Original) - 220 Episodes"},
        {"type": "Series", "title": "Naruto Shippuden"},
        {"type": "Movie", "title": "The Last: Naruto the Movie"},
        {"type": "Series", "title": "Boruto: Naruto Next Generations"}
    ],
    "One Piece": [
        {"type": "Series", "title": "East Blue Saga"},
        {"type": "Series", "title": "Alabasta Saga"},
        {"type": "Series", "title": "Sky Island Saga"},
        {"type": "Series", "title": "Water 7 / Enies Lobby Saga"},
        {"type": "Series", "title": "Thriller Bark / Summit War Saga"},
        {"type": "Series", "title": "Fish-Man Island / Dressrosa Saga"},
        {"type": "Series", "title": "Four Emperors Saga"},
        {"type": "Series", "title": "Final Saga (Ongoing)"}
    ],
    "Jujutsu Kaisen": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Movie", "title": "Jujutsu Kaisen 0 (Prequel)"},
        {"type": "Series", "title": "Season 2 (Hidden Inventory & Shibuya Incident)"}
    ],
    "Demon Slayer": [
        {"type": "Season 1", "title": "Tanjiro Kamado, Unwavering Resolve Arc"},
        {"type": "Movie", "title": "Mugen Train"},
        {"type": "Season 2", "title": "Entertainment District Arc"},
        {"type": "Season 3", "title": "Swordsmith Village Arc"},
        {"type": "Season 4", "title": "Hashira Training Arc"}
    ],
    "Attack on Titan": [
        {"type": "Season 1", "title": "The Fall of Shiganshina"},
        {"type": "Season 2", "title": "The Beast Titan"},
        {"type": "Season 3", "title": "Part 1 & 2 (The Secret of the Basement)"},
        {"type": "Season 4", "title": "The Final Season (Part 1, 2, 3)"}
    ],
    "Code Geass": [
        {"type": "Series", "title": "Lelouch of the Rebellion (Season 1)"},
        {"type": "Series", "title": "Lelouch of the Rebellion R2 (Season 2)"},
        {"type": "Movie", "title": "Lelouch of the Re;surrection"}
    ],
    "Cowboy Bebop": [
        {"type": "Series", "title": "Episodes 1-22"},
        {"type": "Movie", "title": "Knockin' on Heaven's Door"},
        {"type": "Series", "title": "Episodes 23-26"}
    ],
    "Neon Genesis Evangelion": [
        {"type": "Series", "title": "Neon Genesis Evangelion (Original)"},
        {"type": "Movie", "title": "The End of Evangelion"},
        {"type": "Movie", "title": "Evangelion: 1.11, 2.22, 3.33, 3.0+1.0 (Rebuilds)"}
    ],
    "Psycho-Pass": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"},
        {"type": "Movie", "title": "Psycho-Pass: The Movie"},
        {"type": "Series", "title": "Season 3"}
    ],
    "Dr. Stone": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2 (Stone Wars)"},
        {"type": "Special", "title": "Dr. Stone: Ryusui"},
        {"type": "Series", "title": "Season 3 (New World)"}
    ],
    "Re:Zero": [
        {"type": "Series", "title": "Season 1 (Director's Cut)"},
        {"type": "OVA", "title": "Memory Snow"},
        {"type": "OVA", "title": "The Frozen Bond (Prequel)"},
        {"type": "Series", "title": "Season 2"}
    ],
    "Fire Force": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"}
    ],
    "The Promised Neverland": [
        {"type": "Series", "title": "Season 1 (Highly Recommended)"},
        {"type": "Series", "title": "Season 2"}
    ],
    "Blue Lock": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Movie", "title": "Episode Nagi"},
        {"type": "Series", "title": "Season 2"}
    ],
    "Frieren: Beyond Journey's End": [
        {"type": "Series", "title": "Season 1 (Episodes 1-28)"}
    ],
    "Oshi no Ko": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"}
    ],
    "Mushoku Tensei: Jobless Reincarnation": [
        {"type": "Series", "title": "Season 1 (Part 1 & 2)"},
        {"type": "Series", "title": "Season 2"}
    ],
    "That Time I Got Reincarnated as a Slime": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"},
        {"type": "Movie", "title": "Scarlet Bond"},
        {"type": "Series", "title": "Season 3"}
    ],
    "Hellsing": [
        {"type": "Series", "title": "Hellsing Ultimate (OVA Series)"}
    ],
    "Assassination Classroom": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"}
    ],
    "Your Lie in April": [
        {"type": "Series", "title": "Episodes 1-22 (Complete)"}
    ],
    "Violet Evergarden": [
        {"type": "Series", "title": "TV Series (Episodes 1-13)"},
        {"type": "OVA", "title": "Special Episode 14"},
        {"type": "Movie", "title": "Eternity and the Auto Memory Doll"},
        {"type": "Movie", "title": "Violet Evergarden: The Movie"}
    ],
    "Erased": [
        {"type": "Series", "title": "Episodes 1-12 (Complete)"}
    ],
    "Blue Exorcist": [
        {"type": "Series", "title": "Season 1 (Ep 1-17)"},
        {"type": "Series", "title": "Kyoto Saga (Season 2)"},
        {"type": "Series", "title": "Shimane Illuminati Saga (Season 3)"}
    ],
    "The Seven Deadly Sins": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Signs of Holy War"},
        {"type": "Series", "title": "Revival of the Commandments"},
        {"type": "Series", "title": "Imperial Wrath of the Gods"},
        {"type": "Series", "title": "Dragon's Judgement"}
    ],"Fate Series (Unlimited Blade Works Route)": [
        {"type": "Series", "title": "Fate/Zero (Prequel - Watch first for story order)"},
        {"type": "Series", "title": "Fate/stay night: Unlimited Blade Works"},
        {"type": "Movie", "title": "Fate/stay night: Heaven's Feel (I, II, and III)"}
    ],
    "Monogatari Series": [
        {"type": "Series", "title": "Bakemonogatari"},
        {"type": "Series", "title": "Nisemonogatari"},
        {"type": "Movie", "title": "Kizumonogatari (I, II, and III)"},
        {"type": "Series", "title": "Monogatari Series Second Season"},
        {"type": "Series", "title": "Owarimonogatari"}
    ],
    "Bungo Stray Dogs": [
        {"type": "Series", "title": "Season 1 & 2"},
        {"type": "Movie", "title": "Dead Apple"},
        {"type": "Series", "title": "Season 3, 4, and 5"}
    ],
    "Hellsing": [
        {"type": "Series", "title": "Hellsing (2001 - Original)"},
        {"type": "OVA", "title": "Hellsing Ultimate (More faithful to manga)"}
    ],
    "Black Butler": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Book of Circus"},
        {"type": "OVA", "title": "Book of Murder"},
        {"type": "Movie", "title": "Book of the Atlantic"},
        {"type": "Series", "title": "Public School Arc"}
    ],
    "Overlord": [
        {"type": "Series", "title": "Season 1, 2, 3, and 4"},
        {"type": "Movie", "title": "The Holy Kingdom (Upcoming)"}
    ],
    "Fruits Basket": [
        {"type": "Series", "title": "Fruits Basket (2019) - Season 1, 2, and Final Season"},
        {"type": "Movie", "title": "Fruits Basket -prelude-"}
    ],
    "Kaguya-sama: Love is War": [
        {"type": "Series", "title": "Season 1, 2, and 3 (Ultra Romantic)"},
        {"type": "Movie", "title": "The First Kiss That Never Ends"}
    ],
    "Made in Abyss": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Movie", "title": "Dawn of the Deep Spirit"},
        {"type": "Series", "title": "Season 2 (The Golden City of the Scorching Sun)"}
    ],
    "Reincarnated as a Sword": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2 (Announced)"}
    ],
    "Parasyte: The Maxim": [
        {"type": "Series", "title": "Episodes 1-24 (Complete)"}
    ],
    "Great Teacher Onizuka (GTO)": [
        {"type": "Series", "title": "Episodes 1-43 (Complete)"}
    ],
    "Akame ga Kill!": [
        {"type": "Series", "title": "Episodes 1-24 (Complete)"}
    ],
    "Kill la Kill": [
        {"type": "Series", "title": "Episodes 1-24"},
        {"type": "OVA", "title": "Episode 25 (Goodbye Again)"}
    ],
    "Gurren Lagann": [
        {"type": "Series", "title": "Episodes 1-27"},
        {"type": "Movie", "title": "Childhood's End"},
        {"type": "Movie", "title": "The Lights in the Sky are Stars"}
    ],
    "The Melancholy of Haruhi Suzumiya": [
        {"type": "Series", "title": "Season 1 (2006/2009 Chronological Order)"},
        {"type": "Series", "title": "Season 2 (including Endless Eight)"},
        {"type": "Movie", "title": "The Disappearance of Haruhi Suzumiya"}
    ],
    "Cowboy Bebop": [
        {"type": "Series", "title": "Episodes 1-22"},
        {"type": "Movie", "title": "Knockin' on Heaven's Door (Set between Ep 22 & 23)"},
        {"type": "Series", "title": "Episodes 23-26"}
    ],
    "Samurai Champloo": [
        {"type": "Series", "title": "Episodes 1-26 (Complete)"}
    ],
    "Soul Eater": [
        {"type": "Series", "title": "Episodes 1-51 (Complete)"}
    ],
    "Fire Force": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"},
        {"type": "Series", "title": "Season 3 (Announced)"}
    ],
    "Haikyuu!!": [
        {"type": "Series", "title": "Season 1, 2, and 3"},
        {"type": "OVA", "title": "Land vs. Air"},
        {"type": "Series", "title": "Season 4 (To The Top)"},
        {"type": "Movie", "title": "The Dumpster Battle"}
    ],
    "Mob Psycho 100": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"},
        {"type": "Series", "title": "Season 3 (Complete)"}
    ],
    "Noragami": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2 (Aragoto)"}
    ],
    "Clannad": [
        {"type": "Series", "title": "Clannad"},
        {"type": "Series", "title": "Clannad: After Story (The Masterpiece)"}
    ],
    "Danganronpa": [
        {"type": "Series", "title": "Danganronpa: The Animation (Season 1)"},
        {"type": "Game/Summary", "title": "Danganronpa 2 (Goodbye Despair)"},
        {"type": "Series", "title": "Danganronpa 3: Future & Despair Arcs (Alternate episodes)"}
    ],
    "High School DxD": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "New (Season 2)"},
        {"type": "Series", "title": "BorN (Season 3)"},
        {"type": "Series", "title": "Hero (Season 4)"}
    ],
    "Bunny Girl Senpai": [
        {"type": "Series", "title": "Rascal Does Not Dream of Bunny Girl Senpai"},
        {"type": "Movie", "title": "Rascal Does Not Dream of a Dreaming Girl"},
        {"type": "Movie", "title": "Rascal Does Not Dream of a Knapsack Kid"}
    ],
    "Hell's Paradise": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2 (Upcoming)"}
    ],
    "Dr. Stone": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Stone Wars (Season 2)"},
        {"type": "Special", "title": "Ryusui"},
        {"type": "Series", "title": "New World (Season 3)"}
    ],
    "Prison School": [
        {"type": "Series", "title": "Season 1 (Episodes 1-12)"},
        {"type": "OVA", "title": "Mad Wax"}
    ],
    "Berserk": [
        {"type": "Series", "title": "Berserk (1997 - The Golden Age Arc)"},
        {"type": "Movie Trilogy", "title": "The Golden Age Arc I, II, III (Alternative)"},
        {"type": "Series", "title": "Berserk (2016 - Conviction/Falcon of the Millennium Empire)"}
    ],
    "Overlord": [
        {"type": "Series", "title": "Season 1, 2, 3, and 4"},
        {"type": "Movie", "title": "The Holy Kingdom Arc (Upcoming)"}
    ],
    "Blue Lock": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Movie", "title": "Episode Nagi"},
        {"type": "Series", "title": "Season 2"}
    ],
    "Food Wars! (Shokugeki no Soma)": [
        {"type": "Series", "title": "The First Plate"},
        {"type": "Series", "title": "The Second Plate"},
        {"type": "Series", "title": "The Third Plate"},
        {"type": "Series", "title": "The Fourth Plate"},
        {"type": "Series", "title": "The Fifth Plate (Final)"}
    ],
    "Black Lagoon": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "The Second Succession"},
        {"type": "OVA", "title": "Roberta's Blood Trail"}
    ],
    "Hajime no Ippo": [
        {"type": "Series", "title": "The Fighting! (Season 1)"},
        {"type": "TV Special", "title": "Champion Road"},
        {"type": "OVA", "title": "Mashiba vs. Kimura"},
        {"type": "Series", "title": "New Challenger (Season 2)"},
        {"type": "Series", "title": "Rising (Season 3)"}
    ],
    "Initial D": [
        {"type": "Series", "title": "First, Second, Third, and Fourth Stage"},
        {"type": "Series", "title": "Fifth and Final Stage"}
    ],
    "To Your Eternity": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"}
    ],
    "Ranking of Kings": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Special", "title": "The Treasure Chest of Courage"}
    ],
    "Slam Dunk": [
        {"type": "Series", "title": "Episodes 1-101"},
        {"type": "Movie", "title": "The First Slam Dunk (2022)"}
    ],
    "Great Pretender": [
        {"type": "Series", "title": "Season 1 (Cases 1-4)"},
        {"type": "Movie", "title": "Razbliuto"}
    ],
    "Zom 100: Bucket List of the Dead": [
        {"type": "Series", "title": "Season 1 (Episodes 1-12)"}
    ],
    "Hell's Paradise": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2 (Announced)"}
    ],
    "Devilman Crybaby": [
        {"type": "Series", "title": "Episodes 1-10 (Complete)"}
    ],
    "Pluto": [
        {"type": "Series", "title": "Episodes 1-8 (Complete)"}
    ],
    "Classroom of the Elite": [
        {"type": "Series", "title": "Season 1, 2, and 3"}
    ],
    "The Eminence in Shadow": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"},
        {"type": "Movie", "title": "Lost Echoes (Upcoming)"}
    ],
    "Gintama": [
        {"type": "Series", "title": "Gintama (2006)"},
        {"type": "Series", "title": "Gintama' (2011)"},
        {"type": "Series", "title": "Gintama° (2015)"},
        {"type": "Series", "title": "Gintama. (2017)"},
        {"type": "Movie", "title": "Gintama: The Very Final"}
    ],
    "Astra Lost in Space": [
        {"type": "Series", "title": "Episodes 1-12 (Complete Story)"}
    ],
    "Anohana: The Flower We Saw That Day": [
        {"type": "Series", "title": "Episodes 1-11"},
        {"type": "Movie", "title": "Anohana Movie (Summary/Epilogue)"}
    ],
    "Your Name": [
        {"type": "Movie", "title": "Stand-alone Film (By Makoto Shinkai)"}
    ],
    "Weathering With You": [
        {"type": "Movie", "title": "Stand-alone Film (By Makoto Shinkai)"}
    ],
    "Suzume": [
        {"type": "Movie", "title": "Stand-alone Film (By Makoto Shinkai)"}
    ],
    "A Silent Voice": [
        {"type": "Movie", "title": "Stand-alone Film"}
    ],
    "Perfect Blue": [
        {"type": "Movie", "title": "Psychological Thriller (By Satoshi Kon)"}
    ],
    "Death Note": [
        {"type": "Series", "title": "Episodes 1-37 (The Complete Masterpiece)"},
        {"type": "Special", "title": "Death Note: Relight 1 (Visions of a God)"},
        {"type": "Special", "title": "Death Note: Relight 2 (L's Successors)"}
    ],
    "Code Geass": [
        {"type": "Series", "title": "Lelouch of the Rebellion (Season 1)"},
        {"type": "Series", "title": "Lelouch of the Rebellion R2 (Season 2)"},
        {"type": "Movie", "title": "Lelouch of the Re;surrection"}
    ],
    "Banana Fish": [
        {"type": "Series", "title": "Episodes 1-24 (Complete Story)"}
    ],
    "Bungo Stray Dogs": [
        {"type": "Series", "title": "Season 1, 2, and 3"},
        {"type": "Movie", "title": "Dead Apple"},
        {"type": "Series", "title": "Season 4 and 5 (Ongoing)"}
    ],
    "JoJo's Bizarre Adventure": [
        {"type": "Series", "title": "Part 1: Phantom Blood & Part 2: Battle Tendency"},
        {"type": "Series", "title": "Part 3: Stardust Crusaders"},
        {"type": "Series", "title": "Part 4: Diamond is Unbreakable"},
        {"type": "Series", "title": "Part 5: Golden Wind"},
        {"type": "Series", "title": "Part 6: Stone Ocean"}
    ],
    "Hellsing Ultimate": [
        {"type": "OVA", "title": "Episodes 1-10 (Faithful Manga Adaptation)"}
    ],
    "Tokyo Revengers": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Christmas Showdown (Season 2)"},
        {"type": "Series", "title": "Tenjiku Arc (Season 3)"}
    ],
    "Terror in Resonance (Zankyou no Terror)": [
        {"type": "Series", "title": "Episodes 1-11 (Complete)"}
    ],
    "Wonder Egg Priority": [
        {"type": "Series", "title": "Season 1 (Episodes 1-12)"},
        {"type": "Special", "title": "Wonder Egg Priority Special Edition (Ending)"}
    ],
    "Horimiya": [
        {"type": "Series", "title": "Horimiya (Original Season)"},
        {"type": "Series", "title": "Horimiya: The Missing Pieces (Side Stories)"}
    ],
    "Hyouka": [
        {"type": "Series", "title": "Episodes 1-22 (Complete Classic)"}
    ],
    "Gundam: Iron-Blooded Orphans": [
        {"type": "Series", "title": "Season 1 (Episodes 1-25)"},
        {"type": "Series", "title": "Season 2 (Episodes 26-50)"}
    ],
    "The Rising of the Shield Hero": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"},
        {"type": "Series", "title": "Season 3"}
    ],
    "Blue Exorcist": [
        {"type": "Series", "title": "Season 1 (Episodes 1-17)"},
        {"type": "Series", "title": "Kyoto Saga (Season 2)"},
        {"type": "Series", "title": "Shimane Illuminati Saga (Season 3)"}
    ],
    "Overlord": [
        {"type": "Series", "title": "Season 1, 2, 3, and 4"},
        {"type": "Movie", "title": "The Holy Kingdom (Upcoming)"}
    ],
    "Dorohedoro": [
        {"type": "Series", "title": "Season 1 (Episodes 1-12)"},
        {"type": "OVA", "title": "Ma No Omake (Bonus Episodes)"}
    ],
    "KonoSuba": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"},
        {"type": "Movie", "title": "Legend of Crimson"},
        {"type": "Series", "title": "Season 3"}
    ],
    "Log Horizon": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"},
        {"type": "Series", "title": "Destruction of the Round Table (Season 3)"}
    ],
    "Seraph of the End": [
        {"type": "Series", "title": "Vampire Reign (Season 1)"},
        {"type": "Series", "title": "Battle in Nagoya (Season 2)"}
    ],
    "Drifters": [
        {"type": "Series", "title": "Episodes 1-12"},
        {"type": "OVA", "title": "Episodes 13-15"}
    ],
    "Nanana's Buried Treasure": [
        {"type": "Series", "title": "Episodes 1-11 (Complete)"}
    ],
    "Terror in Resonance": [
        {"type": "Series", "title": "Episodes 1-11 (Complete)"}
    ],
    "Charlotte": [
        {"type": "Series", "title": "Episodes 1-13"},
        {"type": "OVA", "title": "The World That Is No Longer Here"}
    ],
    "Angel Beats!": [
        {"type": "Series", "title": "Episodes 1-13 (Complete)"},
        {"type": "Special", "title": "Stairway to Heaven"}
    ],
    "Guilty Crown": [
        {"type": "Series", "title": "Season 1 (Episodes 1-22)"}
    ],
    "Deadman Wonderland": [
        {"type": "Series", "title": "Episodes 1-12"},
        {"type": "OVA", "title": "Red Knife Wielder"}
    ],
    "Darker Than Black": [
        {"type": "Series", "title": "Black Contractor (Season 1)"},
        {"type": "OVA", "title": "Gaiden (Set between S1 and S2)"},
        {"type": "Series", "title": "Gemini of the Meteor (Season 2)"}
    ],
    "No Game No Life": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Movie", "title": "No Game No Life: Zero (Prequel)"}
    ],
    "ReLIFE": [
        {"type": "Series", "title": "Episodes 1-13"},
        {"type": "OVA", "title": "Final Arc (Conclusion)"}
    ],
    "Toradora!": [
        {"type": "Series", "title": "Episodes 1-25 (Complete)"}
    ],
    "The Devil is a Part-Timer!": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2 (Ente Isla Arc)"}
    ],
    "Steins;Gate": [
        {"type": "Series", "title": "Steins;Gate (Episodes 1-22)"},
        {"type": "Special", "title": "Episode 23β (Missing Link)"},
        {"type": "Series", "title": "Steins;Gate 0"},
        {"type": "Series", "title": "Steins;Gate (Episodes 23-24)"},
        {"type": "Movie", "title": "Load Region of Déjà Vu"}
    ],
    "Psycho-Pass": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2"},
        {"type": "Movie", "title": "Psycho-Pass: The Movie"},
        {"type": "Series", "title": "Season 3"},
        {"type": "Movie", "title": "Providence"}
    ],
    "Great Teacher Onizuka": [
        {"type": "Series", "title": "Episodes 1-43 (Complete)"}
    ],
    "Hellsing Ultimate": [
        {"type": "OVA", "title": "Episodes 1-10 (Complete)"}
    ],
    "Cowboy Bebop": [
        {"type": "Series", "title": "Episodes 1-22"},
        {"type": "Movie", "title": "Knockin' on Heaven's Door"},
        {"type": "Series", "title": "Episodes 23-26"}
    ],
    "Neon Genesis Evangelion": [
        {"type": "Series", "title": "Original TV Series"},
        {"type": "Movie", "title": "The End of Evangelion"},
        {"type": "Movie", "title": "Rebuild of Evangelion (1.11, 2.22, 3.33, 3.0+1.0)"}
    ],
    "Samurai Champloo": [
        {"type": "Series", "title": "Episodes 1-26 (Complete)"}
    ],
    "Your Lie in April": [
        {"type": "Series", "title": "Episodes 1-22 (Complete)"}
    ],
    "Clannad": [
        {"type": "Series", "title": "Clannad (Season 1)"},
        {"type": "Series", "title": "Clannad: After Story (Season 2)"}
    ],
    "Durarara!!": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Durarara!!x2 Shou, Ten, and Ketsu"}
    ],
    "Anohana": [
        {"type": "Series", "title": "Episodes 1-11"},
        {"type": "Movie", "title": "Anohana Movie (Epilogue)"}
    ],
    "Kill la Kill": [
        {"type": "Series", "title": "Episodes 1-24"},
        {"type": "OVA", "title": "Goodbye Again (Episode 25)"}
    ],
    "Mob Psycho 100": [
        {"type": "Series", "title": "Season 1, 2, and 3"}
    ],
    "Vinland Saga": [
        {"type": "Series", "title": "Season 1"},
        {"type": "Series", "title": "Season 2 (Slave Arc)"}
    ],
    "Akame ga Kill!": [
        {"type": "Series", "title": "Episodes 1-24 (Complete)"}
    ]
    # You can add the other 47 here following the same pattern!
}