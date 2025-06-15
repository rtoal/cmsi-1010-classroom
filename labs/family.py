class Person:
    def __init__(self, name, mom=None, dad=None, born=None, died=None):
        self.name = name
        self.mom = mom
        self.dad = dad
        self.born = born
        self.died = died

    def life_span(self):
        return f"{self.born or '?'}-{self.died or '?'}"

    def is_sibling_of(self, other):
        """Return if this person is a sibling of the other person."""
        same_mom = self.mom is not None and other.mom is not None and self.mom is other.mom
        same_dad = self.dad is not None and other.dad is not None and self.dad is other.dad
        return same_mom or same_dad

    def is_parent_of(self, other):
        """Return if this person is a parent of the other person."""
        return other is not None and (other.mom is self or other.dad is self)

    def is_child_of(self, other):
        """Return if this person is a child of the other person."""
        return other.is_parent_of(self)

    def is_grandparent_of(self, other):
        """Return if this person is a grandparent of another person."""
        return other is not None and (
            (other.mom is not None and self.is_parent_of(other.mom)) or
            (other.dad is not None and self.is_parent_of(other.dad)))

    def print_family_tree(self, prefix="", level=0):
        """Print the family tree starting from this person."""
        indent = "    " * level
        print(f"{prefix}{self.name} ({self.life_span()})")
        if self.mom:
            self.mom.print_family_tree(f"  {indent}mom: ", level + 1)
        if self.dad:
            self.dad.print_family_tree(f"  {indent}dad: ", level + 1)

    def __str__(self):
        info = f"{self.name} ({self.life_span()})"
        info += f", Mom: {self.mom.name if self.mom else 'Unknown'}"
        info += f", Dad: {self.dad.name if self.dad else 'Unknown'}"
        return info


granbois_7 = Person("Eugénie Granbois", born="bef.1838", died="1907")
baquié_47 = Person("Ferdinand Baquié", born="1837", died="1883")
baquié_46 = Person("Louise Baquié", mom=granbois_7, dad=baquié_47, died="1945")
ramos_1459 = Person("Marie Ramos")
martinez_8709 = Person("Jacques Martinez")
martinez_8708 = Person("Joseph Martinez", mom=ramos_1459, dad=martinez_8709)
martinez_9931 = Person("Adele Martinez", mom=ramos_1459, dad=martinez_8709)
martinez_9927 = Person("Mildred Martinez", mom=baquié_46, dad=martinez_8708)
prevost_1179 = Person("Jeanne Prevost")
fontaine_2773 = Person("Ernest Fontaine")
fontaine_2776 = Person("Suzanne Fontaine", mom=prevost_1179, dad=fontaine_2773)
alioto_37 = Person("Maria Alioto", born="1834", died="aft.1908")
riggitano_1 = Person("Santo Riggitano", born="1824", died="1898")
riggitano_2 = Person("Salvatore Riggitano", mom=alioto_37, dad=riggitano_1)
prevost_1163 = Person("Louis Prevost", mom=fontaine_2776, dad=riggitano_2)
prevost_1162 = Person("Robert Prevost", mom=martinez_9927, dad=prevost_1163)

print(prevost_1162)
print(baquié_47.life_span())
print(martinez_9931.life_span())
print(baquié_46.life_span())
print(martinez_8708.is_sibling_of(martinez_9931))
print(martinez_8708.is_parent_of(martinez_9927))
print(martinez_9927.is_child_of(martinez_8708))
print(martinez_9927.is_grandparent_of(prevost_1162))
prevost_1162.print_family_tree("Robert Prevost: ")
