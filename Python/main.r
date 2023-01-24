library(ggplot2)

# Leer archivo CSV
df <- read.csv("ejemplo.csv", header = TRUE)

# Gráfico de barras de la columna 'Cantidad de ventas bruto'
ggplot(df, aes(x = 1:nrow(df), y = df$`Cantidad de ventas bruto`)) + 
  geom_bar(stat = "identity", fill = "blue") + 
  ggtitle(paste("Total de ventas: $",format(sum(df$`Cantidad de ventas bruto`),big.mark=",",scientific=FALSE))) +
  geom_text(aes(label = ifelse(df$`Cantidad de ventas bruto`!=0, paste0("$",format(df$`Cantidad de ventas bruto`,big.mark=",",scientific=FALSE)),'')), hjust = 0, vjust = -0.5, angle = 45) +
  scale_x_continuous(breaks = 1:nrow(df), labels = 1:nrow(df)) +
  theme(axis.text.x = element_text(angle = 0, hjust = 1))
