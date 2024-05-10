import matplotlib.pyplot as plt

# '/results/mask_cyclegan_vc_<speaker_id_A>_<speaker_id_B>/mask_cyclegan_vc_<speaker_id_A>_<speaker_id_B>.log'파일 값을 data에 삽입 후 실행

data = """
[start of epoch 1]
(epoch: 1, iter: 0, time: 0.198) g_loss: 24.000 d_loss: 0.512 
[end of epoch 1/6172, epoch time: 14]
[start of epoch 2]
(epoch: 2, iter: 0, time: 0.162) g_loss: 24.285 d_loss: 0.499 
[end of epoch 2/6172, epoch time: 14]
[start of epoch 3]
(epoch: 3, iter: 0, time: 0.164) g_loss: 18.968 d_loss: 0.428 
[end of epoch 3/6172, epoch time: 14]
[start of epoch 4]
(epoch: 4, iter: 0, time: 0.165) g_loss: 18.423 d_loss: 0.356 
[end of epoch 4/6172, epoch time: 14]
[start of epoch 5]
(epoch: 5, iter: 0, time: 0.166) g_loss: 18.149 d_loss: 0.377 
[end of epoch 5/6172, epoch time: 14]
[start of epoch 6]
(epoch: 6, iter: 0, time: 0.166) g_loss: 18.281 d_loss: 0.374 
[end of epoch 6/6172, epoch time: 14]
[start of epoch 7]
(epoch: 7, iter: 0, time: 0.167) g_loss: 16.980 d_loss: 0.355 
[end of epoch 7/6172, epoch time: 14]
[start of epoch 8]
(epoch: 8, iter: 0, time: 0.167) g_loss: 16.835 d_loss: 0.355 
[end of epoch 8/6172, epoch time: 14]
[start of epoch 9]
(epoch: 9, iter: 0, time: 0.167) g_loss: 17.004 d_loss: 0.373 
[end of epoch 9/6172, epoch time: 14]
[start of epoch 10]
(epoch: 10, iter: 0, time: 0.167) g_loss: 16.531 d_loss: 0.391 
[end of epoch 10/6172, epoch time: 15]
[start of epoch 11]
(epoch: 11, iter: 0, time: 0.167) g_loss: 16.461 d_loss: 0.369 
[end of epoch 11/6172, epoch time: 14]
[start of epoch 12]
(epoch: 12, iter: 0, time: 0.167) g_loss: 16.387 d_loss: 0.394 
[end of epoch 12/6172, epoch time: 14]
[start of epoch 13]
(epoch: 13, iter: 0, time: 0.167) g_loss: 16.114 d_loss: 0.385 
[end of epoch 13/6172, epoch time: 14]
[start of epoch 14]
(epoch: 14, iter: 0, time: 0.167) g_loss: 16.806 d_loss: 0.407 
[end of epoch 14/6172, epoch time: 14]
[start of epoch 15]
(epoch: 15, iter: 0, time: 0.167) g_loss: 15.707 d_loss: 0.407 
[end of epoch 15/6172, epoch time: 14]
[start of epoch 16]
(epoch: 16, iter: 0, time: 0.168) g_loss: 15.719 d_loss: 0.424 
[end of epoch 16/6172, epoch time: 14]
[start of epoch 17]
(epoch: 17, iter: 0, time: 0.168) g_loss: 15.425 d_loss: 0.407 
[end of epoch 17/6172, epoch time: 14]
[start of epoch 18]
(epoch: 18, iter: 0, time: 0.168) g_loss: 15.178 d_loss: 0.393 
[end of epoch 18/6172, epoch time: 14]
[start of epoch 19]
(epoch: 19, iter: 0, time: 0.168) g_loss: 15.142 d_loss: 0.430 
[end of epoch 19/6172, epoch time: 14]
[start of epoch 20]
(epoch: 20, iter: 0, time: 0.168) g_loss: 15.026 d_loss: 0.429 
[end of epoch 20/6172, epoch time: 15]
[start of epoch 21]
(epoch: 21, iter: 0, time: 0.168) g_loss: 14.662 d_loss: 0.411 
[end of epoch 21/6172, epoch time: 14]
[start of epoch 22]
(epoch: 22, iter: 0, time: 0.168) g_loss: 14.668 d_loss: 0.429 
[end of epoch 22/6172, epoch time: 14]
[start of epoch 23]
(epoch: 23, iter: 0, time: 0.168) g_loss: 16.221 d_loss: 0.421 
[end of epoch 23/6172, epoch time: 14]
[start of epoch 24]
(epoch: 24, iter: 0, time: 0.168) g_loss: 14.450 d_loss: 0.429 
[end of epoch 24/6172, epoch time: 14]
[start of epoch 25]
(epoch: 25, iter: 0, time: 0.168) g_loss: 14.079 d_loss: 0.421 
[end of epoch 25/6172, epoch time: 35]
[start of epoch 26]
(epoch: 26, iter: 0, time: 0.169) g_loss: 14.026 d_loss: 0.429 
[end of epoch 26/6172, epoch time: 14]
[start of epoch 27]
(epoch: 27, iter: 0, time: 0.165) g_loss: 13.762 d_loss: 0.413 
[end of epoch 27/6172, epoch time: 14]
[start of epoch 28]
(epoch: 28, iter: 0, time: 0.166) g_loss: 14.637 d_loss: 0.432 
[end of epoch 28/6172, epoch time: 14]
[start of epoch 29]
(epoch: 29, iter: 0, time: 0.167) g_loss: 14.450 d_loss: 0.414 
[end of epoch 29/6172, epoch time: 14]
[start of epoch 30]
(epoch: 30, iter: 0, time: 0.167) g_loss: 13.663 d_loss: 0.435 
[end of epoch 30/6172, epoch time: 15]
[start of epoch 31]
(epoch: 31, iter: 0, time: 0.167) g_loss: 13.732 d_loss: 0.429 
[end of epoch 31/6172, epoch time: 14]
[start of epoch 32]
(epoch: 32, iter: 0, time: 0.168) g_loss: 13.640 d_loss: 0.411 
[end of epoch 32/6172, epoch time: 14]
[start of epoch 33]
(epoch: 33, iter: 0, time: 0.168) g_loss: 13.688 d_loss: 0.415 
[end of epoch 33/6172, epoch time: 14]
[start of epoch 34]
(epoch: 34, iter: 0, time: 0.168) g_loss: 13.641 d_loss: 0.431 
[end of epoch 34/6172, epoch time: 14]
[start of epoch 35]
(epoch: 35, iter: 0, time: 0.168) g_loss: 13.354 d_loss: 0.435 
[end of epoch 35/6172, epoch time: 14]
[start of epoch 36]
(epoch: 36, iter: 0, time: 0.168) g_loss: 13.435 d_loss: 0.417 
[end of epoch 36/6172, epoch time: 14]
[start of epoch 37]
(epoch: 37, iter: 0, time: 0.168) g_loss: 13.217 d_loss: 0.439 
[end of epoch 37/6172, epoch time: 14]
[start of epoch 38]
(epoch: 38, iter: 0, time: 0.168) g_loss: 12.935 d_loss: 0.419 
[end of epoch 38/6172, epoch time: 14]
[start of epoch 39]
(epoch: 39, iter: 0, time: 0.168) g_loss: 13.030 d_loss: 0.425 
[end of epoch 39/6172, epoch time: 14]
[start of epoch 40]
(epoch: 40, iter: 0, time: 0.168) g_loss: 12.935 d_loss: 0.424 
[end of epoch 40/6172, epoch time: 15]
[start of epoch 41]
(epoch: 41, iter: 0, time: 0.168) g_loss: 12.964 d_loss: 0.426 
[end of epoch 41/6172, epoch time: 14]
[start of epoch 42]
(epoch: 42, iter: 0, time: 0.168) g_loss: 13.094 d_loss: 0.429 
[end of epoch 42/6172, epoch time: 14]
[start of epoch 43]
(epoch: 43, iter: 0, time: 0.168) g_loss: 13.160 d_loss: 0.430 
[end of epoch 43/6172, epoch time: 14]
[start of epoch 44]
(epoch: 44, iter: 0, time: 0.168) g_loss: 13.025 d_loss: 0.426 
[end of epoch 44/6172, epoch time: 14]
[start of epoch 45]
(epoch: 45, iter: 0, time: 0.168) g_loss: 12.970 d_loss: 0.441 
[end of epoch 45/6172, epoch time: 14]
[start of epoch 46]
(epoch: 46, iter: 0, time: 0.168) g_loss: 12.766 d_loss: 0.417 
[end of epoch 46/6172, epoch time: 14]
[start of epoch 47]
(epoch: 47, iter: 0, time: 0.168) g_loss: 12.777 d_loss: 0.427 
[end of epoch 47/6172, epoch time: 14]
[start of epoch 48]
(epoch: 48, iter: 0, time: 0.168) g_loss: 13.331 d_loss: 0.425 
[end of epoch 48/6172, epoch time: 14]
[start of epoch 49]
(epoch: 49, iter: 0, time: 0.168) g_loss: 12.999 d_loss: 0.415 
[end of epoch 49/6172, epoch time: 14]
[start of epoch 50]
(epoch: 50, iter: 0, time: 0.168) g_loss: 12.325 d_loss: 0.429 
[end of epoch 50/6172, epoch time: 36]
[start of epoch 51]
(epoch: 51, iter: 0, time: 0.170) g_loss: 12.690 d_loss: 0.418 
[end of epoch 51/6172, epoch time: 14]
[start of epoch 52]
(epoch: 52, iter: 0, time: 0.165) g_loss: 12.160 d_loss: 0.441 
[end of epoch 52/6172, epoch time: 14]
[start of epoch 53]
(epoch: 53, iter: 0, time: 0.166) g_loss: 12.132 d_loss: 0.439 
[end of epoch 53/6172, epoch time: 14]
[start of epoch 54]
(epoch: 54, iter: 0, time: 0.167) g_loss: 13.025 d_loss: 0.424 
[end of epoch 54/6172, epoch time: 14]
[start of epoch 55]
(epoch: 55, iter: 0, time: 0.167) g_loss: 12.842 d_loss: 0.430 
[end of epoch 55/6172, epoch time: 14]
[start of epoch 56]
(epoch: 56, iter: 0, time: 0.168) g_loss: 12.338 d_loss: 0.425 
[end of epoch 56/6172, epoch time: 14]
[start of epoch 57]
(epoch: 57, iter: 0, time: 0.168) g_loss: 12.832 d_loss: 0.420 
[end of epoch 57/6172, epoch time: 14]
[start of epoch 58]
(epoch: 58, iter: 0, time: 0.168) g_loss: 12.647 d_loss: 0.425 
[end of epoch 58/6172, epoch time: 14]
[start of epoch 59]
(epoch: 59, iter: 0, time: 0.168) g_loss: 12.590 d_loss: 0.432 
[end of epoch 59/6172, epoch time: 14]
[start of epoch 60]
(epoch: 60, iter: 0, time: 0.168) g_loss: 12.782 d_loss: 0.437 
[end of epoch 60/6172, epoch time: 15]
[start of epoch 61]
(epoch: 61, iter: 0, time: 0.168) g_loss: 12.417 d_loss: 0.414 
[end of epoch 61/6172, epoch time: 14]
[start of epoch 62]
(epoch: 62, iter: 0, time: 0.168) g_loss: 12.769 d_loss: 0.431 
[end of epoch 62/6172, epoch time: 14]
[start of epoch 63]
(epoch: 63, iter: 0, time: 0.168) g_loss: 12.460 d_loss: 0.420 
[end of epoch 63/6172, epoch time: 14]
[start of epoch 64]
(epoch: 64, iter: 0, time: 0.168) g_loss: 12.300 d_loss: 0.432 
[end of epoch 64/6172, epoch time: 14]
[start of epoch 65]
(epoch: 65, iter: 0, time: 0.168) g_loss: 12.006 d_loss: 0.425 
[end of epoch 65/6172, epoch time: 14]
[start of epoch 66]
(epoch: 66, iter: 0, time: 0.168) g_loss: 12.243 d_loss: 0.421 
[end of epoch 66/6172, epoch time: 14]
[start of epoch 67]
(epoch: 67, iter: 0, time: 0.168) g_loss: 12.382 d_loss: 0.430 
[end of epoch 67/6172, epoch time: 14]
[start of epoch 68]
(epoch: 68, iter: 0, time: 0.168) g_loss: 11.901 d_loss: 0.428 
[end of epoch 68/6172, epoch time: 14]
[start of epoch 69]
(epoch: 69, iter: 0, time: 0.168) g_loss: 12.056 d_loss: 0.414 
[end of epoch 69/6172, epoch time: 14]
[start of epoch 70]
(epoch: 70, iter: 0, time: 0.168) g_loss: 12.657 d_loss: 0.440 
[end of epoch 70/6172, epoch time: 15]
[start of epoch 71]
(epoch: 71, iter: 0, time: 0.168) g_loss: 12.633 d_loss: 0.436 
[end of epoch 71/6172, epoch time: 14]
[start of epoch 72]
(epoch: 72, iter: 0, time: 0.168) g_loss: 12.023 d_loss: 0.416 
[end of epoch 72/6172, epoch time: 14]
[start of epoch 73]
(epoch: 73, iter: 0, time: 0.168) g_loss: 11.825 d_loss: 0.428 
[end of epoch 73/6172, epoch time: 14]
[start of epoch 74]
(epoch: 74, iter: 0, time: 0.168) g_loss: 11.585 d_loss: 0.427 
[end of epoch 74/6172, epoch time: 14]
[start of epoch 75]
(epoch: 75, iter: 0, time: 0.168) g_loss: 12.005 d_loss: 0.427 
[end of epoch 75/6172, epoch time: 40]
[start of epoch 76]
(epoch: 76, iter: 0, time: 0.166) g_loss: 11.652 d_loss: 0.422 
[end of epoch 76/6172, epoch time: 14]
[start of epoch 77]
(epoch: 77, iter: 0, time: 0.165) g_loss: 11.794 d_loss: 0.441 
[end of epoch 77/6172, epoch time: 14]
[start of epoch 78]
(epoch: 78, iter: 0, time: 0.166) g_loss: 11.612 d_loss: 0.414 
[end of epoch 78/6172, epoch time: 14]
[start of epoch 79]
(epoch: 79, iter: 0, time: 0.167) g_loss: 11.832 d_loss: 0.436 
[end of epoch 79/6172, epoch time: 14]
[start of epoch 80]
(epoch: 80, iter: 0, time: 0.167) g_loss: 11.466 d_loss: 0.418 
[end of epoch 80/6172, epoch time: 15]
[start of epoch 81]
(epoch: 81, iter: 0, time: 0.167) g_loss: 11.663 d_loss: 0.440 
[end of epoch 81/6172, epoch time: 14]
[start of epoch 82]
(epoch: 82, iter: 0, time: 0.168) g_loss: 11.353 d_loss: 0.420 
[end of epoch 82/6172, epoch time: 14]
[start of epoch 83]
(epoch: 83, iter: 0, time: 0.168) g_loss: 11.531 d_loss: 0.427 
[end of epoch 83/6172, epoch time: 14]
[start of epoch 84]
(epoch: 84, iter: 0, time: 0.168) g_loss: 11.864 d_loss: 0.415 
[end of epoch 84/6172, epoch time: 14]
[start of epoch 85]
(epoch: 85, iter: 0, time: 0.168) g_loss: 11.334 d_loss: 0.437 
[end of epoch 85/6172, epoch time: 14]
[start of epoch 86]
(epoch: 86, iter: 0, time: 0.168) g_loss: 11.751 d_loss: 0.420 
[end of epoch 86/6172, epoch time: 14]
[start of epoch 87]
(epoch: 87, iter: 0, time: 0.168) g_loss: 11.535 d_loss: 0.411 
[end of epoch 87/6172, epoch time: 14]
[start of epoch 88]
(epoch: 88, iter: 0, time: 0.168) g_loss: 12.380 d_loss: 0.426 
[end of epoch 88/6172, epoch time: 14]
[start of epoch 89]
(epoch: 89, iter: 0, time: 0.168) g_loss: 11.677 d_loss: 0.443 
[end of epoch 89/6172, epoch time: 14]
[start of epoch 90]
(epoch: 90, iter: 0, time: 0.168) g_loss: 11.525 d_loss: 0.431 
[end of epoch 90/6172, epoch time: 15]
[start of epoch 91]
(epoch: 91, iter: 0, time: 0.168) g_loss: 11.850 d_loss: 0.418 
[end of epoch 91/6172, epoch time: 14]
[start of epoch 92]
(epoch: 92, iter: 0, time: 0.168) g_loss: 12.111 d_loss: 0.424 
[end of epoch 92/6172, epoch time: 14]
[start of epoch 93]
(epoch: 93, iter: 0, time: 0.168) g_loss: 10.905 d_loss: 0.419 
[end of epoch 93/6172, epoch time: 14]
[start of epoch 94]
(epoch: 94, iter: 0, time: 0.168) g_loss: 11.273 d_loss: 0.413 
[end of epoch 94/6172, epoch time: 14]
[start of epoch 95]
(epoch: 95, iter: 0, time: 0.168) g_loss: 12.164 d_loss: 0.422 
[end of epoch 95/6172, epoch time: 14]
[start of epoch 96]
(epoch: 96, iter: 0, time: 0.168) g_loss: 11.497 d_loss: 0.433 
[end of epoch 96/6172, epoch time: 14]
[start of epoch 97]
(epoch: 97, iter: 0, time: 0.168) g_loss: 11.433 d_loss: 0.417 
[end of epoch 97/6172, epoch time: 14]
[start of epoch 98]
(epoch: 98, iter: 0, time: 0.168) g_loss: 11.184 d_loss: 0.422 
[end of epoch 98/6172, epoch time: 14]
[start of epoch 99]
(epoch: 99, iter: 0, time: 0.168) g_loss: 11.145 d_loss: 0.427 
[end of epoch 99/6172, epoch time: 14]
[start of epoch 100]
(epoch: 100, iter: 0, time: 0.168) g_loss: 11.110 d_loss: 0.431 
[end of epoch 100/6172, epoch time: 41]

"""

# 각 에폭과 d_loss, g_loss 값 추출
epochs = []
d_losses = []
g_losses = []
for line in data.split('\n'):
    if 'd_loss' in line:
        parts = line.split()
        epoch = int(parts[1].strip('(),'))
        g_loss = float(parts[5].strip(')'))
        d_loss = float(parts[7].strip(')'))
        epochs.append(epoch)
        d_losses.append(d_loss)
        g_losses.append(g_loss)

# g_loss 그래프 그리기 및 저장
plt.figure(figsize=(10, 5))
plt.plot(epochs, g_losses, marker='o', linestyle='-', color='blue', label='G_Loss')
plt.title('Generator Loss Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('G_Loss')
plt.legend()
plt.grid(True)
plt.savefig('g_loss_graph.png')  # 이미지로 저장
plt.show()

# d_loss 그래프 그리기 및 저장
plt.figure(figsize=(10, 5))
plt.plot(epochs, d_losses, marker='o', linestyle='-', color='red', label='D_Loss')
plt.title('Discriminator Loss Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('D_Loss')
plt.legend()
plt.grid(True)
plt.savefig('d_loss_graph.png')  # 이미지로 저장
plt.show()
