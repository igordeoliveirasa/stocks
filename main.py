import sys


#while True:
    #max_value = float(raw_input("Enter the max stock value: "))
    #print "You must sell when the value reaches: %.2f" %  (max_value - (max_value * 0.15))



if __name__ == "__main__":
    capital = float(raw_input("Total Capital: "))
    capital_risk_rule = 0.02
    capital_risk = capital * capital_risk_rule

    paper_value = float(raw_input("Paper Value: "))
    stop_loss = float(raw_input("Stop Loss: "))
    risk_value_per_paper = paper_value - stop_loss
    paper_amount_to_buy = capital_risk / risk_value_per_paper
    print "%.2f, arredonde sempre para baixo para atingir o lote padrao" % paper_amount_to_buy

