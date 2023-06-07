'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0
    value = "e"
    for item in order.items:
        number_of_amount_zero = ""
        item_amount_list = []
        if value in sorted(str(item.amount)):
            for i in str(item.amount):
                item_amount_list.append(i)
            x = int(item_amount_list.index(value)) + int(1)
            y = int(item_amount_list.index(value)) + int(2)
            number_of_amount_zero = int(str(item_amount_list[x]) + str(item_amount_list[y]))
            j = 1
            real_amount = "1"
            while j <= float(int(number_of_amount_zero)):
                real_amount += "0"
                j = j + 1
            if item.type == 'payment':
                if "-" in item_amount_list:
                    net -= float(real_amount)
                else:
                    net += float(real_amount)
            elif item.type == 'product':
                net -= float(real_amount * item.quantity)
        elif value not in sorted(str(item.amount)):
            if item.type == 'payment':
                net += int(item.amount)
            elif item.type == 'product':
                net -= int(item.amount * item.quantity)
        else:
            return("Invalid item type: %s" % item.type)
    
    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
