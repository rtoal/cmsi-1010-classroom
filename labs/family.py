class Person:
    def __init__(self, name, mom=None, dad=None, born=None, died=None):
        self.name = name
        self.mom = mom
        self.dad = dad
        self.born = born
        self.died = died

    def life_span(self):
        return f"{self.born or '?'}-{self.died or '?'}"

    def __repr__(self):
        """Return a string representation of the person."""
        info = f"{self.name} ({self.life_span()})"
        info += f", Mom: {self.mom.name if self.mom else 'Unknown'}"
        info += f", Dad: {self.dad.name if self.dad else 'Unknown'}"
        return info

    def is_sibling_of(self, other):
        """Check if this person is a sibling of another person."""
        same_mom = self.mom is not None and other.mom is not None and self.mom is other.mom
        same_dad = self.dad is not None and other.dad is not None and self.dad is other.dad
        return same_mom or same_dad

    def is_parent_of(self, other):
        """Check if this person is a parent of another person."""
        return other is not None and (self.mom is other or self.dad is other)

    def is_child_of(self, other):
        """Check if this person is a child of another person."""
        return other.is_parent_of(self)

    def print_family_tree(self, prefix="", level=0):
        """Print the family tree starting from this person."""
        indent = "    " * level
        print(f"{prefix}{self.name} ({self.life_span()})")
        if self.mom:
            self.mom.print_family_tree(f"{indent}mom: ", level + 1)
        if self.dad:
            self.dad.print_family_tree(f"{indent}dad: ", level + 1)


granbois_7 = Person("Eugénie Granbois")
baquié_47 = Person("Ferdinand Baquié")
baquié_46 = Person("Louise Baquié", mom=granbois_7, dad=baquié_47)
ramos_1459 = Person("Marie Ramos")
martinez_8709 = Person("Jacques Martinez", born="1822", died="1891")
martinez_8708 = Person("Joseph Martinez", mom=ramos_1459, dad=martinez_8709)
martinez_9931 = Person("Adele Martinez", mom=ramos_1459, dad=martinez_8709)
martinez_9932 = Person("Gerard Martinez", mom=ramos_1459, dad=martinez_8709)
martinez_9927 = Person("Mildred Martinez", mom=baquié_46, dad=martinez_8708)
prevost_1179 = Person("Jeanne Prevost")
fontaine_2773 = Person("Ernest Fontaine")
fontaine_2776 = Person("Suzanne Fontaine", mom=prevost_1179, dad=fontaine_2773)
alioto_37 = Person("Maria Alioto")
riggitano_1 = Person("Santo Riggitano")
riggitano_2 = Person("Salvatore Riggitano", mom=alioto_37, dad=riggitano_1)
prevost_1163 = Person("Louis Prevost", mom=fontaine_2776, dad=riggitano_2)
prevost_1162 = Person("Robert Prevost", born="1955", mom=martinez_9927, dad=prevost_1163)


prevost_1162.print_family_tree()
