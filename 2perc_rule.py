__author__ = 'igor'


if __name__ == "__main__":
    while True:
        try:
            capital = float(raw_input("Total Capital: "))
            capital_risk_rule = 0.02
            capital_risk = capital * capital_risk_rule

            paper_value = float(raw_input("Paper Value: "))
            stop_loss = float(raw_input("Stop Loss: "))
            risk_value_per_paper = paper_value - stop_loss
            paper_amount_to_buy = capital_risk / risk_value_per_paper
            print "%.2f, arredonde sempre para baixo para atingir o lote padrao" % paper_amount_to_buy
            if (paper_amount_to_buy * paper_value > capital):
                print "Mas voce nao tem capital para isso, voce pode comprar no maximo: %.2f" % (capital/paper_value)
            raw_input()
        except:
            pass