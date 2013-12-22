$(document).ready(function(){
   $('input.search-page').typeahead({
      name: 'accounts',
      local: ["Coone", "CJ Bolland", "Avicii", "Umek", "Dillon Francis", "Stafford Brothers", "Tony Humphries", "DJ Rush", "Krafty Kuts", "Q-Bert", "Dave Pearce", "Da Tweekaz", "Diplo", "Mike Koglin", "John Digweed", "Terry Francis", "Sandra Collins", "CJ Mackintosh", "Adam Sheridan", "Mark Knight", "Josh Wink", "Ricky Stone", "D-Formation", "Miss Kittin", "Junior Vasquez", "Dion Mavath", "DJ Dan", "Meat Katie", "Jimmy Van M", "Krewella", "Pete Tong", "Sander Van Doorn", "Bobina", "Christian Cambas", "James Holden", "Lisa Lashes", "Diego Miranda", "Dave Angel", "John Peel", "Richie Hawtin", "Judge Jules", "Super8 & Tab", "Joris Voorn", "Freddy Fresh", "Gui Boratto", "Matthias Hellbronn", "Knife Party", "Misstress Barbara", "Scot Project", "Agnelli & Nelson", "R3hab", "Angel Moraes", "Bingo Players", "Sharam", "Mark Farina", "Richard Durand", "John Acquaviva", "Desyn Masiello", "DJ Sammy", "Mauro Picotto", "Justice", "Harvey", "Dimitri Vegas & Like Mike", "Rachel Aubern", "Joachim Garraud", "Sander Kleinenberg", "Max Graham", "Dubfire", "Pete The Zouk", "Brisk", "Carl Craig", "John B", "Roni Size", "Chris Leibing", "Armand Van Helden", "D-Block & S-Te-Fan", "Marcus Schossow", "Jimpy", "Adam Beyer", "Booka Shade", "Astral Projection", "Graeme Park", "Markus Schulz", "DJ EZ", "Full Intention", "Parks and Wilson", "Blasterjaxx", "Nervo", "Madeon", "Sean Tyas", "Mat Zo", "Allister Whitehead", "X-Press 2", "Deep Dish", "Afrojack", "Ummet Ozcan", "Noisecontrollers", "Mike Candys", "Darude", "DJ Hercio", "Erol Alkan", "Paul Oakenfold", "Frankie Knuckles", "Christopher Lawrence", "Dope Smugglaz", "Scratch Perverts", "Eddie Halliwell", "Nick Warren", "Gigi D'Agostino", "Vicetone", "Dieselboy", "Tocadisco", "Alan Thompson", "Chris Fortier", "Norman Cook", "MYNC Project", "Mario Piu", "Nero", "Satoshi Tomiie", "Tim Deluxe", "Stonebridge", "Yoji Biomehanika", "JFK", "Deadmau5", "Mrs Wood", "Juan Atkins", "Felix Da Housecat", "Victor Calderone", "Kerri Chandler", "Laurent Wolf", "Steve Porter", "Matt Jam Lamont", "Surgeon", "Infected Mushroom", "Solar System", "Gilles Peterson", "Benjamin Bates", "Goldie", "Filo & Peri", "Danny Tenaglia", "Chris Liebing", "Quentin Mosimann", "Rank 1", "Boy George", "Daniel Kandi", "Matt Cantor", "DJ Die", "Frank Trax", "Arty", "Myon & Shane 54", "Derrick May", "Nic Fanciulli", "Sied Van Riel", "D.A.V.E the Drummer", "Project 46", "Alesso", "Signum", "George Acosta", "Hernan Cattaneo", "Tom Stephan", "Norman Jay", "Stanton Warriors", "Swedish House Mafia", "Sasha", "Mark Moore", "Mr C", "Aly & Fila", "DJ Hype", "Doc Martin", "Felguk", "Timo Maas", "Sidney Samson", "Donald Glaude", "Andy C", "Steve Hurley", "ATB", "Yousef", "Andrew Rayel", "Psyko Punkz", "The Chemical Brothers", "Marco Bailey", "Neelix", "Fabio", "DJ Feel", "Chuckie", "Sebastien Leger", "DJ Rap", "Paul Glazby", "DJ Skazi", "DJ Luna", "Francois K", "Doc Scott", "Kaskade", "The Dreem Team", "Dada Life", "Gabriel & Dresden", "Francis Davila", "Dirty South", "Robbie Rivera", "Hixxy", "Steve Lawler", "Dannic", "Pippi", "Phil Kieran", "Proteus", "Patrick Forge", "Zinc", "Mixmaster Mike", "Boys Noize", "Claudia Cazacu", "Dougal", "Hardwell", "Masters At Work", "Moshic", "Thomas Gold", "Marco V", "Orjan Nilsen", "Dyro", "Showtek", "Ran-D", "Basement Jaxx", "Angerfist", "Roger Shah", "Eric Prydz", "Lee Burridge", "M.I.K.E. Push", "Lottie", "John Graham", "Jeremy Healy", "Fatboy Slim", "Greg Downey", "Bl3nd", "Laidback Luke", "Adam Freeland", "David Holmes", "Tenashar", "W & W", "Layo & Bushwacka", "Ian M", "Tritonal", "Matt Darey", "Jonathan Lisle", "Tom Middleton", "Queen Maxine", "Fergie", "Paul Kalkbrenner", "Stu Allen", "Rob Tissera", "Tenishia", "Lady Dana", "Simon Patterson", "Menno De Jong", "Paul Trouble Anderson", "Ronski Speed", "Andy Farley", "Lange", "Anderson Noise", "DJ Sy", "Marco Carola", "David Morales", "Flash Brothers", "AN21", "Cosmic Gate", "Talla 2 XLC", "DJ Marky", "Marcel Woods", "Kyau & Albert", "Colin Tevendale", "Funkmaster Flex", "Nicky Romero", "Martin Solveig", "Ricardo Villalobos", "DJ Heaven", "Lisa Pin-up", "James Lavelle", "DJ Sneak", "Calvin Harris", "Darren Emerson", "Seb Fontaine", "Michel De Hey", "Claudio Coccoluto", "Andy Morris", "Scott K", "Chris Coco", "Tony De Vit", "Alex Morph & Woody Van Eyden", "Leon Bolier", "Astrix", "Mickey Finn", "Skrillex", "Chus & Ceballos", "Guy Ornadel", "Craig Richards", "DJ Crust", "Danny Rampling", "Miss Jo Lively", "Juanjo Martin", "Andy Weatherall", "Dave Lee/Joey Negro", "DJs From Mars", "Billy Nasty", "Wildstylez", "Jose Padilla", "Darren Pearce", "Porter Robinson", "Nick Sentience", "Derrick Carter", "Luke Fair", "Craig Dimech", "Ronald van Gelderen", "Coldcut", "Tuff Jam", "DJ Randall", "Heatbeat", "Junior Jack", "Tommy Trash", "Anne Savage", "Karl Tuff Enuff Brown", "Sonique", "Tydi", "Paul Van Dyk", "Aphrodite", "Dash Berlin", "Wrecked Machines", "Graham Gold", "Ferry Corsten", "Hype", "Ashley Casselle", "Martin Garrix", "Westbam", "Sister Bliss", "Laurent Garnier", "Kai Tracid", "Slam", "Jeff Mills", "Adaro", "LTJ Bukem", "Pete Wardman", "Bob Sinclar", "Omnia", "BK", "BT", "Solarstone", "Gareth Emery", "DJ Disciple", "Tiesto", "Chris & James", "Lord G", "Marco Lenzi", "DJ Vibe", "Shogun", "DJ Tatana", "Ariel", "Joe Clausell", "Tidy Boys", "Above & Beyond", "Dave Clarke", "Wally Lopez", "Carl Cox", "Anthony Pappa", "Alex M.O.R.P.H.", "Todd Terry", "Tom Wainwright", "Cor Fijneman", "Alex P", "James Zabiela", "Daft Punk", "David Guetta", "Smokin Jo", "Bloody Beetroots", "Tall Paul", "Moonbeam", "Zedd", "Tiddey", "Wolfgang Gartner", "Arnej", "Valentino Kanzyani", "Brennan Heart", "Danny Howells", "Pete Heller", "Tiga", "Slipmatt", "Zatox", "Wasted Penguinz", "Sven Vath", "Steve Thomas", "Ian Ossia", "Remy", "Jon The Dentist", "Scott Bond", "Sharkey", "Gordon Kaye", "The Thrillseekers", "Dave Seaman", "John O'Callaghan", "Simon Posford", "Antoine Clamaran", "Joy Kitikonti", "Blu Peter", "Lisa Loud", "Matt Hardwick", "Erick Morillo", "Headhunterz", "Boris Dlugosch", "DJ Shadow", "Hybrid", "Phil Smart", "Magda", "Jon Carter", "Feed Me", "Armin Van Buuren", "Dave Lee", "Fedde Le Grand", "2manyDJs", "Steve Angello", "Bad Boy Bill", "Harri", "Mr Scruff", "Steve Aoki", "Roger Sanchez", "Luciano", "Slacker", "Antoine", "Frontliner", "Brandon Block", "Force & Styles", "Justin Robertson", "Blank & Jones", "Andy Smith", "DJ Tarkan", "Jon Pleased Wimmin", "Ashley Beedle", "Martin Garcia", "John 00 Fleming", "Grooverider", "Andy Moor", "Dimitri From Paris", "Offer Nissim", "John Kelly", "Colin Dale", "Chris Liberator", "Axwell", "Amadeus", "Netsky", "Gunz For Hire", "Serge Devant", "Cass", "Plump DJs", "Yahel", "Johan Gielen", "Sebastian Ingrosso", "Axel Karakasis", "Trentemoller", "Benny Benassi"],
      template: '<p>{{value}}</p>',
      engine: Hogan
    });

    $('#chart').highcharts({
            chart: {
                zoomType: 'xy',
                width: 800
            },
            title: {
                text: 'DJMag Top 100 Rankings'
            },
            xAxis: {
                title: {
                    enabled: true,
                    text: 'Year'
                },
                showLastLabel: true,
                labels: {
                    format: "{value}"
                }
            },
            yAxis: {
                title: {
                    text: 'Rank'
                },
                reversed: "true",
                min: 1
            },
            plotOptions: {
                scatter: {
                    marker: {
                        radius: 5,
                        states: {
                            hover: {
                                enabled: true,
                                lineColor: 'rgb(100,100,100)'
                            }
                        }
                    },
                    states: {
                        hover: {
                            marker: {
                                enabled: false
                            }
                        }
                    },
                    tooltip: {
                        headerFormat: '<b>{series.name}</b><br>',
                        pointFormat: '{point.x}, #{point.y}'
                    }
                }
            },
            series: [{
                name: 'Steve Angello',
                data: [[2006,66],[2007,46],[2008,63],[2009,20],[2010,14],[2011,23],[2012,57],[2013,38]]

            }, {
                name: 'Axwell',
                data: [[2006,93],[2007,33],[2008,20],[2009,14],[2010,10],[2011,12],[2012,23],[2013,19]]
            },{
                name: 'Sebastian Ingrosso',
                data: [[2009,25],[2010,16],[2011,26],[2012,34],[2013,18]]
            }]
        });
});
