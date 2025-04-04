class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        super().__init__("Visitor is not vaccinated."
                         " A vaccine key is required.")


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        super().__init__("Visitor's vaccine is outdated."
                         " A valid vaccine is required.")


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        super().__init__("Visitor is not wearing a mask. A mask is required.")
