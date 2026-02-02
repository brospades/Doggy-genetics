class Dog:
    "All dogs created by user"

    def __init__(
        self,
        master,
        dog_genotype,
        dog_pretty_genotype,
        dog_pretty_result,
        dog_comp,
        dog_icon,
        dog_name="My dog",
    ):
        self.genotype = dog_genotype  # Pairs of selected alleles for each locus
        self.pretty_genotype = dog_pretty_genotype  # Gene + desc

        # Name
        if master.dog_name.get():
            dog_name = master.dog_name.get()
        self.name = dog_name
        if len(self.name) > 12:
            self.name = self.name[:10] + ".."

        # Text result
        self.desc = " ".join(list(dog_pretty_result.values()))[:19] + ".."

        # Fullsize dog image
        self.comp = dog_comp
        # Dog icon
        self.icon = dog_icon
