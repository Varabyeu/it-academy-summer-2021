""" Модель из жизни
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ. Создайте
несколько объектов классов, которые описывают ситуацию. Объекты
должны содержать как атрибуты так и методы класса для симуляции
различных действий. Программа должна инстанцировать объекты и
эмулировать какую-либо ситуацию - вызывать методы, взаимодействие
объектов и т.д.

Модель: оценка заказа на выполнение работ.
Оценка подразумевает под собой сопоставление сложности работ с их
стоимостью и сроками выполнения.
order_name - наименование работы (строительство ТЭЦ)
order_object - объект работы (ТЭЦ)
order_type - тип работы (новое строительство)
order_terms - сроки выполнения работ(48 месяцев)
order_price - стоимость услуги ($10 000 000)
order_start_date - отсрочка старта выполнения заказа (в месяцах)
"""
from inspect import getmembers
from inspect import isfunction


class OrderData:
    """Docstring

    This class get order data and makes
     packages to transfer to departments
     """

    def __init__(self, order_name, order_object,
                 order_type, order_terms, order_price,
                 prepaid_expense, order_start_date):
        self.name = order_name
        self.object = order_object
        self.type = order_type
        self.terms = order_terms
        self.price = order_price
        self.prepaid = prepaid_expense
        self.start_date = order_start_date

    def order_data_tech(self):
        tech_data_order = {
            'Order name': self.name,
            'Object': self.object,
            'Type of order': self.type,
            'Terms': self.terms,
            'Months before the beginning': self.start_date
        }
        return tech_data_order

    def order_data_marketing(self):
        order_data_marketing = {
            'Order name': self.name,
            'Terms (months)': self.terms,
            'Order price (USA doll.)': self.price,
            'Prepaid': self.prepaid,
            'Months before the beginning': self.start_date
        }
        return order_data_marketing


class TechDepAnalysis:
    curr_staff_employment = 8

    def __init__(self, tech_data):

        self.name = tech_data.get('Order name')
        self.object = tech_data.get('Object')
        self.type = tech_data.get('Type of order')
        self.terms = tech_data.get('Terms (months)')
        self.start_date = tech_data.get('Months before the beginning')

    def analysis_object(self):
        possible_objects = ['power plant', 'boiler plant',
                            'hydroelectric power plant',
                            'solar power plant',
                            'wind power plant',
                            'biogas power plant',
                            'geothermal power plant']

        if self.object.lower() not in possible_objects:
            object_verdict = 'We cannot do this order.'
            object_status = False
        else:
            object_verdict = 'It is OK. We can do this.'
            object_status = True
        return object_verdict, object_status

    def analysis_type_object(self):
        possible_type_objects = ['new construction', 'reconstruction',
                                 'modernization']

        if self.type.lower() not in possible_type_objects:
            object_type_verdict = 'We cannot do this order. We have not enough' \
                                  'qualification.'
            type_status = False
        else:
            object_type_verdict = 'It is OK. We have qualification in this.'
            type_status = True
        return object_type_verdict, type_status

    def analysis_terms(self):

        if self.start_date < self.curr_staff_employment:
            terms_verdict = 'Impossible. ' \
                            'Need to adjust the start date or ' \
                            'cancel this order.'
            terms_status = False
        else:
            terms_verdict = 'It is OK. We can start today.'
            terms_status = True
        return terms_verdict, terms_status

    def final_analysis(self):
        analyzes = [self.analysis_object()[1],
                    self.analysis_type_object()[1],
                    self.analysis_terms()[1]]
        if all(analyzes) is True:
            final_verdict = 'We can get this order and complete it.'
        else:
            final_verdict = 'We not able to complete this order. '
            if analyzes[0] is False:
                final_verdict += 'We have never completed' \
                                 ' similar objects.'
            elif analyzes[1] is False:
                final_verdict += 'We have never completed' \
                                 ' similar type objects.'
            elif analyzes[2] is False:
                final_verdict += 'We have no enough time to do this.'
        return final_verdict


class MarketDepartmentAnalysis:
    cost_price_month_work = 10000
    curr_fin_balance = 200000

    def __init__(self, marketing_data):
        self.marketing_data = marketing_data
        self.name = marketing_data.get('Order name')
        self.terms = marketing_data.get('Terms (months)')
        self.price = marketing_data.get('Order price (USA doll.)')
        self.prepaid = marketing_data.get('Prepaid')
        self.start_date = marketing_data.get('Months before'
                                             ' the beginning')

    def fin_situation(self):
        staff_employment = getattr(TechDepAnalysis,
                                   'curr_staff_employment')
        cost_monthly = self.cost_price_month_work * staff_employment
        budget_load_end = self.curr_fin_balance - cost_monthly
        if budget_load_end > 0:
            budget_status_end = 'good'
        else:
            budget_status_end = 'bad'
        return staff_employment, budget_load_end, cost_monthly, budget_status_end

    def analysis_terms(self):
        tech_terms = TechDepAnalysis(order.order_data_tech()).analysis_terms()
        if tech_terms[1] is True:
            terms_status = 'It is real.'
        else:
            terms_status = 'It is unreal. We cannot use our specialists.'
        return terms_status

    def analysis_price(self):
        cost_monthly = self.fin_situation()[2]
        if self.price / self.terms >= cost_monthly:
            price_status = 'Price satisfies.'
        else:
            price_status = 'Price is too low.'
        return price_status

    def analysis_prepaid(self):
        if self.prepaid > 0:
            if self.prepaid < 15:
                prepaid_status = 'Prepaid not satisfies.' \
                                 ' Will be better to raise it.'
            else:
                prepaid_status = 'Prepaid satisfies.'
        return prepaid_status

    def analysis_start_date(self):
        if self.fin_situation()[1] > 0:
            start_date_verdict = 'We have enough finance to ' \
                                 'wait a few weeks.'
            start_date_status = True
        else:
            start_date_verdict = 'We need in finance to work stably.'
            start_date_status = False

        return start_date_verdict, start_date_status

    def analysis_finally(self):

        all_obj = getmembers(MarketDepartmentAnalysis)
        list_all_func = [f[0] for f in all_obj if isfunction(f[1])]
        all_defs = []
        for func in list_all_func[2:]:
            call_def = getattr(MarketDepartmentAnalysis, func)
            all_defs.append(call_def)
            if all(all_defs) is True:
                final_verdict = 'It is interesting order.'
            else:
                final_verdict = 'We have got some doubts.'
            return final_verdict


order = OrderData('Power plant construction', 'Power plant',
                  'New construction', 48, 10000000, 10, 7)

tech_dep = TechDepAnalysis(order.order_data_tech())
tech_verdict_terms = tech_dep.analysis_terms()
tech_verdict_object = tech_dep.analysis_object()
tech_verdict_type_object = tech_dep.analysis_type_object()
tech_verdict_final_verdict = tech_dep.final_analysis()
marketing_dep = MarketDepartmentAnalysis(order.order_data_marketing())
mark_terms = marketing_dep.analysis_price()

with open('Contract_evaluation_report.txt', 'w') as report:
    report.writelines([
        'Object name: {}\n\n'.format(order.name),
        'Technical department verdict:\n\n',
        'Terms: {}\n'.format(tech_verdict_terms[0]),
        'Object: {}\n'.format(tech_verdict_object[0]),
        'Type of object: {}\n'.format(tech_verdict_type_object[0]),
        'Finally: {}\n'.format(tech_verdict_final_verdict),
        '\nMarketing department verdict:\n\n',
        'Finance situation overwiew:\n',
        'Current balance is ${}'.format(marketing_dep.curr_fin_balance),
        ', monthly ',
        'cost price is ${}.\n'.format(marketing_dep.fin_situation()[2]),
        'At the end of available orders financial balance will be',
        ' ${}. \nIt is {}.'.format(marketing_dep.fin_situation()[1],
                                   marketing_dep.fin_situation()[3]),
        '\n\nFinance aspects of potential order:\nTerms:{}\n'.format(
            marketing_dep.analysis_terms()),
        'Price: {}\n'.format(marketing_dep.analysis_price()),
        'Prepayment: {}\n'.format(marketing_dep.analysis_prepaid()),
        'Start of the order: {}\n'.format(marketing_dep.analysis_start_date()[0]),
        'Finally: {}\n\n'.format(marketing_dep.analysis_finally()),
        'SUMMARY:\n',
        'You should consider this order more carefully'])
