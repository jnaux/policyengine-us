from policyengine_us.model_api import *


class va_personal_exemption_spouse(Variable):
    value_type = float
    entity = TaxUnit
    label = "Virginia aged/blind exemption"
    defined_for = StateCode.VA
    unit = USD
    definition_period = YEAR
    reference = "https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf#page=19"

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.va.tax.income.spouse_head_adjustment
        age_spouse = tax_unit("age_spouse", period)
        age_blind_spouse = tax_unit("blind_spouse", period) + (
            age_spouse >= p.age_threshold
        )

        personal_exemption_spouse = (
            age_blind_spouse * p.age_blind_multiplier + p.addition_amount
        )

        return personal_exemption_spouse