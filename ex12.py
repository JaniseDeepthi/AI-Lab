# Input values 
P_H = 0.005  # Prior: P(Disease) 
P_not_H = 1 - P_H  # Complement: P(No Disease) 
 
P_E_given_H = 0.98       # Likelihood: P(Positive Test | Disease) 
P_E_given_not_H = 0.02   # False Positive Rate: P(Positive Test | No Disease) 
 
# Total probability of a positive test (evidence)
P_E = (P_E_given_H * P_H) + (P_E_given_not_H * P_not_H) 
 
# Bayes' Theorem: Posterior = (Likelihood * Prior) / Evidence
P_H_given_E = (P_E_given_H * P_H) / P_E

# Output result
print("P(Disease | Positive Test) =", round(P_H_given_E, 4))

