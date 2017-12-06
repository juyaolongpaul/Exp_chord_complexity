__author__ = 'rhapsody0710'
import os
from numpy import *
import math
from pprint import pprint
dataFile = 'result.txt'
DirPrefix = ".." + os.path.sep + "Results" + os.path.sep
LabelIndex = {"15_glot": 1, "15_glot_sp": 2,
              "15_spap_nmod4": 3}
IndexLabel = ["", "15_glot", "15_glot_sp", "15_spap_nmod4"]

with open(DirPrefix + dataFile) as f:
    d = [x.strip() for x in f.readlines() if not x.startswith('#')]

dataList = os.listdir(DirPrefix)
r = len(d) / 60 * 10
m = 3
M = m * (m - 1) / 2
Scores = zeros((r+1, m+1, m+1))
count = {}

for line in d:
    labels = line.split(':')[0]
    label1 = labels.split(',')[0][:labels.split(',')[0].rfind('_')]
    label2 = labels.split(',')[1][:labels.split(',')[1].rfind('_')]
    score = int(line.split(':')[-1])
    if count.has_key(label1 + label2):
        count[label1 + label2] += 1
    else:
        count[label1 + label2] = 1
    # print line
    # print i+1
    # print LabelIndex[label1]
    # print LabelIndex[label2]
    Scores[count[label1 + label2]][LabelIndex[label1]][LabelIndex[label2]] = (0 - float(score))

mu_hat = zeros((m+1, m+1))
for i in range(1, m + 1):
    for j in range(1, m + 1):
        for k in range(1, r + 1):
            mu_hat[i][j] += Scores[k][i][j] / float(r)

pi_hat = zeros((m+1, m+1))
for i in range(1, m + 1):
    for j in range(1, m + 1):
        pi_hat[i][j] = 0.5 * (mu_hat[i][j] - mu_hat[j][i])

delta_hat = zeros((m+1, m+1))
for i in range(1, m + 1):
    for j in range(1, m + 1):
        delta_hat[i][j] = 0.5 * (mu_hat[i][j] + mu_hat[j][i])

alpha_hat = zeros((m+1))
for i in range(1, m + 1):
    for j in range(1, m + 1):
        alpha_hat[i] += pi_hat[i][j] / float(m)

gamma_hat = zeros((m+1, m+1))
for i in range(1, m + 1):
    for j in range(1, m + 1):
        gamma_hat[i][j] = pi_hat[i][j] - alpha_hat[i] + alpha_hat[j]


S_mu = 0.0
for i in range(1, m + 1):
    for j in range(1, m + 1):
        S_mu += mu_hat[i][j] * mu_hat[i][j]
S_mu *= float(r)

S_pi = 0.0
for i in range(1, m + 1):
    for j in range(i + 1, m + 1):
        S_pi += pi_hat[i][j] * pi_hat[i][j]
S_pi *= float(r) * 2.0

S_delta = 0.0
for i in range(1, m + 1):
    for j in range(1, i):
        S_delta += delta_hat[i][j] * delta_hat[i][j]
S_delta *= float(r) * 2.0

S_alpha = 0.0
for i in range(1, m + 1):
    S_alpha += alpha_hat[i] * alpha_hat[i]
S_alpha *= float(m) * float(r) * 2.0

S_gamma = 0.0
for i in range(1, m + 1):
    for j in range(i + 1, m + 1):
        S_gamma += gamma_hat[i][j] * gamma_hat[i][j]
S_gamma *= float(r) * 2.0

S_error = 0.0
for i in range(1, m + 1):
    for j in range(1, m + 1):
        for k in range(1, r + 1):
            S_error += (Scores[k][i][j] - mu_hat[i][j]) * (Scores[k][i][j] - mu_hat[i][j])

sigma2 = S_error / float(2 * M * (r - 1))

S_t = 0.0
for i in range(1, m + 1):
    for j in range(1, m + 1):
        for k in range(1, r + 1):
            S_t += Scores[k][i][j] * Scores[k][i][j]


print IndexLabel
print alpha_hat

print "S_mu: %f" % S_mu
print "S_pi: %f" % S_pi
print "S_alpha: %f" % S_alpha
print "S_t: %f" % S_t
print "----------"
print "S_delta: %f" % S_delta
print "S_gamma: %f" % S_gamma
print "S_error: %f" % S_error
print "sigma2: %f" % sigma2
print "The Yardstick is supposed to be %f * q (m = %d, df = %d)" % (math.sqrt(sigma2 / (2 * r * m)), m, 2 * M * (r - 1))

