#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

class Solution(object):
    def distance(self, p1, p2):
        d = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        return d

    def triangleArea(self, threepoints):
        ret_area = 0
        if len(threepoints) != 3:
            return ret_area
        point_one = threepoints[0]
        point_two = threepoints[1]
        point_three = threepoints[2]

        a = self.distance(point_one, point_two)
        b = self.distance(point_one, point_three)
        c = self.distance(point_two, point_three)
        # no triangle
        if not (a + b > c and a + c > b and b + c > a):
            return ret_area

        p = (a + b + c) / 2.0
        ret_area = math.sqrt(p * (p - a) * (p - b) * (p -c))

        return ret_area

            
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # 1 任意取三个点
        points_set = []
        points_num = len(points)
        for i in range(0, points_num):
            for j in range(i + 1, points_num):
                for k in range(j + 1, points_num):
                    cur_element = [points[i], points[j], points[k]]
                    points_set.append(cur_element)

        # 2 三角形面积公式
        max_area = 0
        for one in points_set:
            cur_area = self.triangleArea(one)
            if cur_area > max_area:
                max_area = cur_area
                    
        return max_area
        
if __name__ == "__main__":
     obj = Solution()
     points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
     print obj.largestTriangleArea(points)
     
     p1 = [1, 0]
     p2 = [0, 1]
     # print obj.distance(p1, p2)
