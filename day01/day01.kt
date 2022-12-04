/**
 * Advent of Code 2022 Day 1 solution.
 */

import java.io.File

val testinp = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
  """.trimIndent()

private fun solve_day01_pt1(inp: String): Int {
  val lol = inp.split("\n\n").map{ it.split("\n").map{ it.toInt() } }
  val lolsums = lol.map{ it.sum() }
  return lolsums.max()
}

private fun solve_day01_pt2(inp: String): Int {
  val lol = inp.split("\n\n").map{ it.split("\n").map{ it.toInt() } }
  val lolsums = lol.map{ it.sum() }
  //println(lolsums::class.java.typeName)
  //println(lolsums[0]::class.java.typeName)
  val top3 = lolsums.sortedDescending().slice(0..2)
  return top3.sum()
}

//fun main(args: Array<String>){
fun main(){
  var res = solve_day01_pt1(testinp)
  println("day 01 pt 1 test-out=$res")

  val inp = File("./in/day01.in").readText().trim()
  res = solve_day01_pt1(inp)
  println("day 01 pt 1 result=$res")

  res = solve_day01_pt2(testinp)
  println("day 01 pt 2 test-out=$res")

  res = solve_day01_pt2(inp)
  println("day 01 pt 2 result=$res")
}
