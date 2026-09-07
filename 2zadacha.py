num_managers = 15
salary_per_month = 120_000
time_saving_on_routine = 0.20
routine_time_share = 0,30
sales_growth_rate = 0.08
current_annual_revenue = 72_000_000
crm_cost_per_user_year = 24_000
training_months = 1
horizon_years = 3
discount_rate = 0.12
tax_rate = 0.20

annual_salary_saving = num_managers * salary_per_month * 12 * rountine_time_share * time_saving_on_rountine

annual_revenue_increase = current_annual_revenue * sales_growth_rate

total_licensing_cost = num_managers * crm_cost_per_user_year * horizon_years

training_losses = num_managers * salary_per_month * training_months

annual_gross_profit = annual_salary_saving + annual_revenue_increase - (num_managers * crm_cost_per_user_year)

net_annual_profit = annual_gross_profit * (1-tax_rate)

cash_flows = [-training_losses] + [net_annual_profit] * horizon_years

npv = sum([cf / (1 + discount_rate)**i for i, cf in enumerate(cash_flows)])

payback_period = abs(cash_flows[0]) / net_annual_profit

total_net_profit = net_annual_profit * horizon_years

roi = (total_net_profit - training_losses) / training_loses

print(f"Годовая экономия ФОТ: {annual_salary_saving:,.0f} руб.")
print(f"Дополнительный доход в год: {annual_revenue_increase:,.0f} руб.")
print(f"Чистая прибыль в год(после налога): {net_annual_profit:,.0f} руб.")
print(f"NPV проекта: {npv:,.0f} руб.")
print(f"Срок окупаемости: {payback_period:,.2f} руб.")
print(f"ROI: {roi*100:,.1f} руб.")
