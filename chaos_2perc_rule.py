__author__ = 'igor'

import random

def randrange_float(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start


if __name__ == "__main__":
    capital = 120000 #float(raw_input("Total Capital: "))

    for i in range(0,800):
        try:
            capital_risk_rule = 0.02
            capital_risk = capital * capital_risk_rule


            while True:
                try:
                    paper_value = 22#float(raw_input("Paper Value: "))
                    break
                except:
                    continue

            entrance = paper_value

            while True:
                try:
                    stop_loss = 21#float(raw_input("Stop Loss: "))
                    break
                except:
                    continue

            risk_value_per_paper = paper_value - stop_loss
            paper_amount_to_buy = capital_risk / risk_value_per_paper
            print "%.2f, arredonde sempre para baixo para atingir o lote padrao" % paper_amount_to_buy
            if (paper_amount_to_buy * paper_value > capital):
                print "Mas voce nao tem capital para isso, voce pode comprar no maximo: %.2f" % (capital/paper_value)


            while True:
                try:
                    paper_to_buy_count = paper_amount_to_buy#float(raw_input("Sendo assim, Quantos papeis deseja comprar?"))
                    break
                except:
                    continue

            capital = capital - (paper_to_buy_count * entrance)

            while True:
                percent = randrange_float(-3, 3, 0.3)
                if percent >= 0:
                    paper_value += (paper_value * (abs(percent)/100))
                else:
                    paper_value -= (paper_value * (abs(percent)/100))

                print "Novo valor para a variacao de %.2f%%: %.2f" % (percent, paper_value)

                if paper_value <= stop_loss:
                    capital = capital + (stop_loss * paper_to_buy_count)
                    print "Stop loss disparado em %.2f!" % (stop_loss)
                    break
                else:
                    print "Lucro Atual: %.2f" % ((paper_value-entrance)*paper_to_buy_count)

                    while True:
                        try:
                            #answer = raw_input("Deseja vender? (S,N)")
                            break
                        except:
                            continue

                    if ((paper_value-entrance)*paper_to_buy_count) > 20:
                        capital = capital + (paper_value * paper_to_buy_count)
                        break

                    #if answer in ("S", "s"):
                    #    capital = capital + (paper_value * paper_to_buy_count)
                    #    break

            print "Novo Capital: %.2f" % (capital)
        except:
            pass