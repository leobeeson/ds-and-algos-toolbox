 

# Height of Stacked Boxes: source -> https://www.youtube.com/watch?v=aPQY__2H3tE&ab_channel=Reducible
def can_be_stacked(top_box: tuple[int, int, int], bottom_box: tuple[int, int, int]) -> bool:
    return top_box[0] < bottom_box[0] and top_box[1] < bottom_box[1]

def tallest_stack(boxes: list[tuple]) -> int:
    boxes.sort(key=lambda x: x[0])
    heights = {box:box[2] for box in boxes}
    for i in range(1, len(boxes)):
        box = boxes[i]
        stack = [boxes[j] for j in range(i) if can_be_stacked(boxes[j], box)]
        heights[box] = box[2] + max([heights[stacked_box] for stacked_box in stack], default=0)
    return max(heights.values(), default=0)

boxes = [(4,5,3), (2,3,2), (3,6,2), (1,5,4), (2,4,1), (1,2,2)]
tallest_stack(boxes)

