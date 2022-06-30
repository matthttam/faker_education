from faker.providers import BaseProvider
from random import choice, sample, randint
from .constants import school_list


class SchoolProvider(BaseProvider):
    def school_object(self):
        """Returns a random airport dict. Example:
        {
            "school": "Madison Elementary School",
            "district": "Groveport Madison Local",
            "level": "Elementary",
            "type": "Regular school",
            "state": "OH",
            "nces_id": "390469702730",
        }
        """
        school_object = choice(school_list)
        return school_object

    def school_name(self):
        school = self.school_object()
        name = school.get("school")
        return name

    def school_level(self):
        school = self.school_object()
        level = school.get("level")
        return level

    def school_type(self):
        school = self.school_object()
        school_type = school.get("type")
        return school_type

    def school_district(self):
        school = self.school_object()
        district = school.get("district")
        return district

    def school_state(self):
        school = self.school_object()
        state = school.get("state")
        return state

    def school_nces_id(self):
        school = self.school_object()
        nces_id = school.get("nces_id")
        return nces_id
