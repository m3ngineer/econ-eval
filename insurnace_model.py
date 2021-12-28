'''
Consider the following scenarios:

Scenario 1: There is a 0.1% chance in any given year that you get into a serious car accident. If this happens then you will incur medical bills that cost about $300,000 (assume the care post accident is non-discretionary and there is not external financial support). You have the option of buying insurance that costs $30/month that will cover the cost associated with the accident in full.

Scenario 2: There’s a 20% chance that you get into a minor bicycle accident in a year. If this happens then you incur a medical bill that costs about $1,500. You can buy insurance that costs $30/month to cover this cost in full.


If you could only choose one, which scenario would you buy insurance for?

Here’s the problem: we’re not all the same, and not everyone has the same risks. You might think that the fairest way to create risk pools is to only pool together people of comparable risks. However, a pool that is exclusively composed of very sick people will face unaffordable premiums, and this raises distributional concerns. Different problems arise when we try to pool enrollees with diverse health profiles, because healthier, less expensive enrollees might not want to subsidize those in their pool who are sicker and will spend more. It’s this latter problem that we’re going to focus on here. If the healthier individuals drop out of the risk pool because they do not want to pay a premium that reflects the sicker people in their pool, that is known as adverse selection.

Actuarially Fair Premiums
Let’s dig deeper into actuarially fair premiums (the amount of money that an insurer can expect to pay out in medical expenses for an individual or risk pool) and how they work in practice.
Suppose we consider the example of two twin brothers, David and Michael, who have identical health status.
They both have access to insurance through their employers. Their total spending on health care (insurer plus out of pocket payments for care) is listed below.

Average total medical spending (including cost sharing) by David and Michael under different insurance policies
 	                   David    |   Michael
10% cost sharing    |  $15,000	|   $15,000
30% cost sharing	|  $12,000	|   $12,000

Q1:
What is the actuarially fair premium for David if he buys the 10% cost sharing plan?

Since the actuarially fair premium is the amount of money that an insurer can expect to pay out in medical expenses for an individual or risk pool, let’s calculate what that amount is for David.
It is not the whole $15,000 since he is enrolled in a 10% cost sharing plan, so we have to deduct the amount David will pay out of his own pocket. As a result the answer is:
$13,500 = $15,000 - (10% * $15,000)

Q2:
What is the actuarially fair premium for Michael if he buys the 30% cost sharing plan?


$8,400 = $12,000 - (30% * $12,000)

In this scenario, what are one or two reasons why the actuarially fair premium for Michael in the 30% cost sharing plan is less than the actuarially fair premium for David in the 10% cost sharing plan?

One explanation is that the actuarially fair premium does not include cost sharing, so the insurer pays a smaller share of the medical spending in Michael’s case since he is buying the 30% cost sharing plan whereas David is buying the 10% cost sharing plan. Another explanation is that there is less moral hazard in the less generous insurance plan. (Remember from Module 2 that moral hazard is the increase in health care utilization associated with insurance, which happens when patients do not feel the full burden of paying for health care.) In the 10% cost sharing plan, patients are responsible for a smaller percentage of total health care spending than in the 30% cost sharing plan, so patients might be overconsuming health care on the 10% plan, resulting in higher total medical spending for the 10% cost sharing plan.

Notice that the actuarially fair premium does not include the out-of-pocket costs. The amount that the insurance company is expected to spend is the amount that is included in the actuarially fair premium.
'''

med_expenses = 15000
cost_sharing = 0.1
afp = med_expenses - (cost_sharing * med_expenses)
print(afp)

# Adverse Selection
'''
An employer offers two health plans. One is a PPO plan with a very wide set of in-network physicians. Another is an HMO with a wide set of in-network PCPs, but a more restricted network of specialists and hospitals. Apart from the network, the benefit designs are the same, so assume that a person’s out-of-pocket spending will not differ across plans.

Consider 5 individuals who are choosing between the two insurance plans:

Isabella is a 25-year-old woman who competes in triathlons, and she rarely gets sick. If she has a health-related issue, her primary concern is finding the first doctor with availability.
Health status: 10/10.
Taysir is a 36-year-old man who works as a sports instructor. He has mild asthma which is triggered when he occasionally smokes. He does not have established relationships with any doctors.
Health status: 9/10.
Tom is a 73-year-old man who is in relatively good health and exercises regularly. He can feel himself slowing down as he ages, and is quite anxious about his health. He likes regular check-ups with his primary care physician that he has been seeing for over 30 years.
Health status: 7/10.
Yemane is a 40-year-old woman who has cardiovascular disease as well as a family history of heart disease. She is particular about which doctor she visits.
Health status: 5/10.
Nelly is a 57-year-old woman who was diagnosed with diabetes a few years ago. However, with the support of her new primary care doctor she is starting to reach normal blood sugar levels without medication, and feels better than she has in years. She is extremely choosy about which doctors she will see for her care.
Health status: 4/10.

Each of these people is willing to pay for access to a broader network of specialists.

 	Health status	AFP	Willingness to pay (WTP) for HMO	Willingness to pay (WTP) for PPO
Isabella	10/10	6800	7000
Taysir	9/10	8000	8500
Tom	7/10	9500	10200
Yemane	5/10	11000	12000
Nelly	4/10	15000	17000
Fill in estimates of WTP for the PPO in the table above. The exact numbers do not matter; we are looking for the relationship between health status and the incremental WTP for the PPO vs the HMO.

We require two conditions to hold for an accurate estimate of numbers:

WTP for HMO < WTP for PPO (as each individual is willing to pay for access to a broad network of specialists)
The difference between the WTP for the HMO, and the WTP for the PPO increases as health status gets worse. In other words, sicker individuals are more willing to pay for access to a broad network of specialists. So, for example, Taysir is willing to pay $1,000 more for the PPO plan (vs. the HMO plan), while Nelly is willing to pay $5,000 more for the PPO plan.
In the prompt, we weren’t given information of whether the sicker individuals’ PCPs and other specialists are in the HMO network or not. However, there is less of a chance that their preferred PCPs and specialists are in the HMO network than in the PPO network. This further explains why sicker individuals are willing to pay more for the PPO Plan.

 	Health status	AFP	WTP for HMO	WTP for PPO
Isabella	10/10	6800	7000	7500
Taysir	9/10	8000	8500	9500
Tom	7/10	9500	10200	13500
Yemane	5/10	11000	12000	16000
Nelly	4/10	15000	17000	22000

'''
