from recipe_scrapers.mykitchen101en import MyKitchen101en
from tests import ScraperTest


class TestMyKitchen101enScraper(ScraperTest):

    scraper_class = MyKitchen101en

    def test_host(self):
        self.assertEqual("mykitchen101en.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Mykitchen101en Team", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Baked Mini Egg Sponge Cakes", self.harvester_class.title())

    def test_yields(self):
        self.assertEqual("30 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://mykitchen101en.com/wp-content/uploads/2020/11/mini-baked-egg-sponge-cake-mykitchen101en-feature.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 eggs (grade A/size: L)",
                "125 g fine sugar",
                "⅛ tsp fine salt",
                "115 g plain flour",
                "20 g cornstarch",
                "30 g melted butter",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Preheat oven to 200°C/395°F.\nBeat eggs & sugar\nBeat eggs lightly, add in salt and sugar, beat until combined.\nPrepare warm water\nCombine 1 Liter of plain water with 400 ml of hot water (from electric thermo pot) in a large steel bowl to yield warm water with temperature about 45°C/113°F.\nbeat egg mixture until stiff\nDip mixing bowl in warm water bath, beat egg mixture over medium-high speed until stiff (about 5 minutes). (Reminder: Beating egg mixture over warm water will shorten the time for it to become stiff.)\nSift flour\nCombine plain flour and cornstarch, sift twice.\nAdd flour to egg mixture, add in melted butter\nAdd flour to egg mixture gradually, mix over low speed, fold until well mixed with spatula. Add in melted butter gradually, fold gently until mixed with spatula.\nPour batter into piping bags.\nFill batter in mini muffin pans\nLine mini muffin pans (diameter = 4.8 cm, depth = 2.2 cm) with cupcake liners, fill with batter until 80% full.\nBake in the preheated oven at 190°C/375°F for 20-22 minutes, until golden brown. (Reminder: The heat for different oven is different, the suggested time is only for reference, adjust the baking time base on your oven if necessary. If the 1st batch has 24 pieces of cakes, the 2nd batch will only have 6 pieces, then the baking time for 2nd batch can be shortened, just bake until they are golden brown.)\nUnmould & cool\nUnmould and cool mini egg sponge cakes on wire rack.",
            self.harvester_class.instructions(),
        )
