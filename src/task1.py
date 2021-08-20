""" Модель из жизни
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ. Создайте
несколько объектов классов, которые описывают ситуацию. Объекты
должны содержать как атрибуты так и методы класса для симуляции
различных действий. Программа должна инстанцировать объекты и
эмулировать какую-либо ситуацию - вызывать методы, взаимодействие
объектов и т.д.
Модель: оценка заказа на выполнение работ.

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
        """Docstring

        Analysis is used to compare complexity of the works with its
        price and terms.
        order_name - name of the object (строительство ТЭЦ)
        order_object - object describe(ТЭЦ)
        order_type - work type(новое строительство)
        order_terms -work terms in month(48)
        order_price - consumer price in dollars(10 000 000)
        order_start_date -start of of the work since today in months(2)
        prepaid_expense - count with prepaid
        """
        self.name = order_name
        self.object = order_object
        self.type = order_type
        self.terms = order_terms
        self.price = order_price
        self.prepaid = prepaid_expense
        self.start_date = order_start_date

    def order_data_tech(self):
        """Making dictionary

        This function makes dictionary using the inputted
        data which is need to post to marketing department
        """

        tech_data_order = {
            'Order name': self.name,
            'Object': self.object,
            'Type of order': self.type,
            'Terms': self.terms,
            'Months before the beginning': self.start_date
        }
        return tech_data_order

    def order_data_marketing(self):
        """Making dictionary

        This function makes dictionary using the inputted
        data which is need to post to marketing department
        """
        order_data_marketing = {
            'Order name': self.name,
            'Terms (months)': self.terms,
            'Order price (USA doll.)': self.price,
            'Prepaid': self.prepaid,
            'Months before the beginning': self.start_date
        }
        return order_data_marketing


class TechDepAnalysis:
    """Class docstring

    This class is processing inputted data end existing conditions
    to make verdict: is this object can be fulfilled by department
    or not
    """
    curr_staff_employment = 8

    def __init__(self, tech_data):
        """In this method makes variables defined"""
        self.name = tech_data.get('Order name')
        self.object = tech_data.get('Object')
        self.type = tech_data.get('Type of order')
        self.terms = tech_data.get('Terms (months)')
        self.start_date = tech_data.get('Months before the beginning')

    def analysis_object(self):
        """Comparing possibility

        This function compares current object with lists of possible
        objects to work. If current object in list - this work can be
        fulfilled
        """
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
        """Do the organization have enough skills to do project

        This function compares current object with lists of skills in
        building objects. If current object in list - this work can be
        fulfilled
        """
        possible_type_objects = ['new construction', 'reconstruction',
                                 'modernization']

        if self.type.lower() not in possible_type_objects:
            object_type_verdict = 'We cannot do this order. ' \
                                  'We have not enough' \
                                  'qualification.'
            type_status = False
        else:
            object_type_verdict = 'It is OK. We have qualification in this.'
            type_status = True
        return object_type_verdict, type_status

    def analysis_terms(self):
        """Function analyzes current load and and determines can the
        organization do this work in this terms
        """
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
        """Function gives final verdict of department"""

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


class MarketDepAnalysis:
    """Docstring

    This class is processing inputted data end existing conditions
    to make verdict: is this object can be fulfilled by department
    or not
    """
    cost_price_month_work = 10000
    curr_fin_balance = 200000

    def __init__(self, marketing_data):
        """In this method makes variables defined"""
        self.marketing_data = marketing_data
        self.name = marketing_data.get('Order name')
        self.terms = marketing_data.get('Terms (months)')
        self.price = marketing_data.get('Order price (USA doll.)')
        self.prepaid = marketing_data.get('Prepaid')
        self.start_date = marketing_data.get('Months before'
                                             ' the beginning')

    def fin_situation(self):
        """Function analyzes current financial situation to determine how necessary
        this object"""
        stf_mplmnt = getattr(TechDepAnalysis,
                             'curr_staff_employment')
        cst_mothl = self.cost_price_month_work * stf_mplmnt
        budget_load_end = self.curr_fin_balance - cst_mothl
        if budget_load_end > 0:
            bdgt_stts_nd = 'good'
        else:
            bdgt_stts_nd = 'bad'
        return stf_mplmnt, budget_load_end, cst_mothl, bdgt_stts_nd

    def analysis_terms(self):
        """This function analyzes terms by current load"""
        tech_terms = TechDepAnalysis(order.order_data_tech()).analysis_terms()
        if tech_terms[1] is True:
            terms_status = 'It is real.'
        else:
            terms_status = 'It is unreal. We cannot use our specialists.'
        return terms_status

    def analysis_price(self):
        """This function analyzes the customer's proposal as a whole"""
        cost_monthly = self.fin_situation()[2]
        if self.price / self.terms >= cost_monthly:
            price_status = 'Price satisfies.'
        else:
            price_status = 'Price is too low.'
        return price_status

    def analysis_prepaid(self):
        """Function analyzes the customer's proposal in prepaid"""
        if self.prepaid > 0:
            if self.prepaid < 15:
                prepaid_status = 'Prepaid not satisfies.' \
                                 ' Will be better to raise it.'
            else:
                prepaid_status = 'Prepaid satisfies.'
        return prepaid_status

    def analys_start(self):
        """Function makes a conclusion about the desired start date"""
        if self.fin_situation()[1] > 0:
            start_date_verdict = 'We have enough finance to ' \
                                 'wait a few weeks.'
            start_date_status = True
        else:
            start_date_verdict = 'We need in finance to work stably.'
            start_date_status = False

        return start_date_verdict, start_date_status

    def analysis_finally(self):
        """Function gives final verdict of department"""
        all_obj = getmembers(MarketDepAnalysis)
        list_all_func = [f[0] for f in all_obj if isfunction(f[1])]
        all_defs = []
        for func in list_all_func[2:]:
            call_def = getattr(MarketDepAnalysis, func)
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
market_dep = MarketDepAnalysis(order.order_data_marketing())
mark_terms = market_dep.analysis_price()

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
        'Current balance is ${}'.format(market_dep.curr_fin_balance),
        ', monthly ',
        'cost price is ${}.\n'.format(market_dep.fin_situation()[2]),
        'At the end of available orders financial balance will be',
        ' ${}. \nIt is {}.'.format(market_dep.fin_situation()[1],
                                   market_dep.fin_situation()[3]),
        '\n\nFinance aspects of potential order:\nTerms:{}\n'.format(
            market_dep.analysis_terms()),
        'Price: {}\n'.format(market_dep.analysis_price()),
        'Prepayment: {}\n'.format(market_dep.analysis_prepaid()),
        'Start of the order: {}\n'.format(market_dep.analys_start()[0]),
        'Finally: {}\n\n'.format(market_dep.analysis_finally()),
        'SUMMARY:\n',
        'You should consider this order more carefully'])
