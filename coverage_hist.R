#!/usr/bin/R

# Invoke % R --slave --args coverage.txt coverage.png < coverage.R

Args    <- commandArgs()
stats   <- Args[4]
outplot <- Args[5]

data <- read.table(stats,sep="\t")
png(outplot, width=960, height=960, pointsize=24)
plot(data[,3],type="h",main="Genome Coverage", xlab="Depth of Coverage", ylab="Count", col="red", xlim=c(0,3000), ylim=c(0,200000))
dev.off()